document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll('.skill-item').forEach((item) => {
    const para = item.querySelector('p');

    item.addEventListener('mouseenter', () => {
      para.style.display = 'block'; // show paragraph
    });

    item.addEventListener('mouseleave', () => {
      para.style.display = 'none'; // hide paragraph
    });
  });
});
