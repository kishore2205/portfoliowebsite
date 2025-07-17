
function showTab(id) {
  document.querySelectorAll("section").forEach(section => {
    section.classList.remove("active");
  });
  document.getElementById(id).classList.add("active");
}

function calculateAge() {
    const dobInput = document.getElementById('dob');
    const ageInput = document.getElementById('age');

    if (!dobInput.value) return;

    const birthDate = new Date(dobInput.value);
    const today = new Date();

    let age = today.getFullYear() - birthDate.getFullYear();
    const monthDiff = today.getMonth() - birthDate.getMonth();

    // adjust if birthday hasn't occurred yet this year
    if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }

    ageInput.value = age >= 0 ? age : '';
}

