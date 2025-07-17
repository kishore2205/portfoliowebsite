const expTitles = document.querySelectorAll('.exp-title');

expTitles.forEach(title => {
  title.addEventListener('click', () => {
    const content = title.nextElementSibling;
    const isVisible = content.style.display === "block";

    // Close all others
    document.querySelectorAll('.exp-content').forEach(c => c.style.display = "none");

    // Toggle current
    content.style.display = isVisible ? "none" : "block";
  });
});
