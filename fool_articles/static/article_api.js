(function() {
  const BASE_URL = "/";
  const ArticleAPI = {
    comments: {
      getComments: () => {
        return fetch(`${BASE_URL}comments/`)
          .then(response => response.json())
          .then(responseJson => {
            // Show some elements
          });
      },
      submitComment: ({ text, username }) => {
        return fetch(`${BASE_URL}comments/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
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
      ArticleAPI.comments.submitComment({ username, text: commentText });
    });
  }
})();
