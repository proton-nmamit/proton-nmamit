document.getElementById('username').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        const username = this.value;
        document.querySelector('.output').innerHTML += `<p>Username: ${username}</p>`;
        this.style.display = 'none';
        document.getElementById('password').style.display = 'block';
        document.getElementById('password').focus();
    }
});

document.getElementById('password').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        const password = this.value;
        document.querySelector('.output').innerHTML += `<p>Password: ${password}</p>`;
        // Here you can add your login logic
        alert('Login submitted!');
    }
});

document.getElementById('submit').addEventListener('click', function () {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    alert(`Username: ${username}\nPassword: ${password}`);
});