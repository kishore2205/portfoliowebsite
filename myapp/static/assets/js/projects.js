document.addEventListener("DOMContentLoaded", () => {
  const projectBoxes = document.querySelectorAll('.project-box');

  projectBoxes.forEach(box => {
    box.addEventListener('mouseenter', () => {
      // Remove 'active' class from all other boxes
      projectBoxes.forEach(el => {
        if (el !== box) {
          el.classList.remove('active');
        }
      });

      // Add 'active' class to current box
      box.classList.add('active');
    });

    box.addEventListener('mouseleave', () => {
      // Optional: Remove active class on mouse leave
      box.classList.remove('active');
    });
  });
});
