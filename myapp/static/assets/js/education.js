// Select all buttons
const titles = document.querySelectorAll('.edu-title');

titles.forEach(title => {
  title.addEventListener('click', () => {
    // Toggle visibility of the next sibling (edu-content)
    const content = title.nextElementSibling;
    const isVisible = content.style.display === "block";

    // Close all other contents
    document.querySelectorAll('.edu-content').forEach(c => c.style.display = "none");

    // Toggle current
    content.style.display = isVisible ? "none" : "block";
  });
});
