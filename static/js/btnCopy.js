(function () {
  const copyLink = document.getElementById("copy-link");

  if (copyLink === null) {
    return;
  }

  copyLink.addEventListener("click", async (e) => {
    e.preventDefault();
    await navigator.clipboard.writeText(window.location.href);

    const icon = copyLink.querySelector("i");
    icon.className = "bi bi-clipboard-check";
    copyLink.lastChild.textContent = " Copied";

    setTimeout(() => {
      icon.className = "bi bi-clipboard";
      copyLink.lastChild.textContent = " Copy link";
    }, 2000);
  });
})();
