(function() {
  function getCookie(name) {
    // Verbatim from django docs on csrf
    // https://docs.djangoproject.com/en/3.0/ref/csrf/
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      var cookies = document.cookie.split(";");
      for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  const BASE_URL = "/article";
  const ArticleAPI = {
    comments: {
      getComments: articleId => {
        return fetch(`${BASE_URL}/${articleId}/comments/list`).then(response =>
          response.json()
        );
      },
      submitComment: ({ text, username, articleId }) => {
        const csrfToken = getCookie("csrftoken");
        return fetch(`${BASE_URL}/${articleId}/comments/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken,
            "X-Requested-With": "XMLHttpRequest"
          },
          body: JSON.stringify({
            text,
            username
          })
        })
          .then(response => response.json())
          .catch(e => {
            // Show to user?
          });
      }
    }
  };

  function getCommentsHandler(data) {
    const comments = data.comment_list;
    const commentContainer = document.getElementById("comment-container");
    comments.forEach(function(comment) {
      const commentElement = document.createElement("div");
      commentElement.className = "comment row";
      const text = document.createElement("p");
      text.innerHTML = comment.text;
      text.className = "comment-text";
      const username = document.createElement("h5");
      username.innerHTML = comment.username || "Anonymous";
      username.className = "user";
      const createdAt = document.createElement("span");
      createdAt.innerHTML = new Date(comment.created_at).toLocaleString();
      createdAt.className = "date";

      commentElement.appendChild(username);
      commentElement.appendChild(createdAt);
      commentElement.appendChild(text);

      commentContainer.appendChild(commentElement);
    });
  }

  if (Article != undefined && Article.id != null) {
    ArticleAPI.comments.getComments(Article.id).then(getCommentsHandler);
  }

  const submitCommentButton = document.querySelector("#submit-comment");
  if (submitCommentButton != null) {
    submitCommentButton.addEventListener("click", function(e) {
      e.preventDefault();
      const username = document.getElementById("comment-username").value;
      const commentText = document.getElementById("comment-text").value;
      if (commentText == null || commentText.trim() == "") {
        // TODO - add error class to textarea
        return;
      }
      ArticleAPI.comments
        .submitComment({
          username,
          text: commentText,
          articleId: Article.id
        })
        .then(() => {
          window.alert("Successfully submitted comment!");
          document.getElementById("comment-container").innerHTML = "";
          ArticleAPI.comments.getComments(Article.id).then(getCommentsHandler);
        });
    });
  }
})();
