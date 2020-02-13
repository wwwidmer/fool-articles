"use strict";
(function() {
  function shuffleChildren(rootElement, childSelector) {
    const children = rootElement.querySelectorAll(childSelector);

    rootElement.innerHTML = "";
    // Fancy code alert
    // Math.random creates a number from 0 to 1, subtracting 0.5 causes a potential for a negative number
    // which gives us -n, 0, and n which sort uses to determine the place of the element.
    const shuffledChildren = Array.from(children).sort(
      () => Math.random() - 0.5
    );

    for (const child of shuffledChildren) rootElement.appendChild(child);
  }

  const button = document.querySelector(".shuffle-button");
  if (button != null) {
    button.addEventListener("click", function() {
      shuffleChildren(document.getElementById("stock-list"), ".stock-row");
    });
  }
})();
