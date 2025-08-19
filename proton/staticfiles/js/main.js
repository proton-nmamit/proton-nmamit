var before = document.getElementById("before");
var liner = document.getElementById("liner");
var command = document.getElementById("typer"); 
var textarea = document.getElementById("texter"); 
var terminal = document.getElementById("terminal");

var git = 0;
var pw = false;
let pwd = false;
var commands = [];
var currentUser = window.username || 'user'; // Use the username from Django context

var loginStep = 0;
var loginCredentials = {
    username: '',
    password: ''
};

var isPasswordInput = false;
var tempPassword = '';

// Add mobile detection and optimization
const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
let hasInitialized = false;

// Single initialization function
function initializeTerminal() {
    if (!hasInitialized) {
        textarea.focus();
        updatePrompt(window.username || 'user');
        loopLines(home, "", isMobile ? 40 : 80);
        hasInitialized = true;
    }
}

// Remove all other initialization calls and use only DOMContentLoaded
document.addEventListener('DOMContentLoaded', initializeTerminal);

// Keep focus handler
document.addEventListener('click', function() {
    textarea.focus();
});

window.addEventListener("keyup", enterKey);

textarea.value = "";
command.innerHTML = textarea.value;

function typeIt(e) {
    command.innerHTML = e.value;
}

function moveIt(count, event) {
    if (event.keyCode === 37 || event.keyCode === 39) {
        return;
    }
    command.innerHTML = textarea.value;
}

function enterKey(e) {
  if (e.keyCode == 181) {
    document.location.reload(true);
  }
  if (e.keyCode == 13) { // Enter key
    const inputText = textarea.value;
    commands.push(inputText);
    git = commands.length;
    
    // Modify this section to mask password
    if (loginStep === 1 && isPasswordInput) {
      addLine(`${currentUser}@proton:~$ ${'*'.repeat(tempPassword.length)}`, "no-animation", 0);
    } else {
      addLine(`${currentUser}@proton:~$ ${inputText}`, "no-animation", 0);
    }
    
    if (loginStep === 1) {
      handleLoginInput(isPasswordInput ? tempPassword : inputText);
    } else {
      commander(inputText.toLowerCase());
    }
    
    command.innerHTML = "";
    textarea.value = "";
    tempPassword = '';
  } else if (loginStep === 1 && isPasswordInput) {
    // Handle password input
    if (e.keyCode === 8) { // Backspace
      if (tempPassword.length > 0) {
        tempPassword = tempPassword.slice(0, -1);
        command.innerHTML = '*'.repeat(tempPassword.length);
      }
    } else if (e.key.length === 1) { // Regular character
      tempPassword += e.key;
      command.innerHTML = '*'.repeat(tempPassword.length);
    }
    e.preventDefault();
  } else {
    if (pw) {
      let et = "*";
      let w = textarea.value.length;
      command.innerHTML = et.repeat(w);
      if (textarea.value === password) {
        pwd = true;
      }
      if (pwd && e.keyCode == 13) {
        loopLines(secret, "color2 margin", 120);
        command.innerHTML = "";
        textarea.value = "";
        pwd = false;
        pw = false;
        liner.classList.remove("password");
      } else if (e.keyCode == 13) {
        addLine("Wrong password", "error", 0);
        command.innerHTML = "";
        textarea.value = "";
        pw = false;
        liner.classList.remove("password");
      }
    } else {
      if (e.keyCode == 38 && git != 0) {
        git -= 1;
        textarea.value = commands[git];
        command.innerHTML = textarea.value;
      }
      if (e.keyCode == 40 && git != commands.length) {
        git += 1;
        if (commands[git] === undefined) {
          textarea.value = "";
        } else {
          textarea.value = commands[git];
        }
        command.innerHTML = textarea.value;
      }
    }
  }
}

  
function commander(cmd) {
  const fullCommand = cmd.toString().trim();
  const parts = fullCommand.split(' ');
  const command = parts[0].toLowerCase();
  
  switch (command) {
    case "help":
      loopLines(help, "color2 margin", 80);
      break;
    case "about":
      loopLines(about, "color2 margin", 80);
      break;
    // Add Rick Roll triggers
    case "proton":
    case "roshan":
    case "shyam":
    case "manjunath":
    case "prashith":
    case "rishi":
    case "prashit":
      addLine("You've been Rick Rolled!", "color2 margin", 0);
      playRickRoll();
      break;
    case "yash":
      addLine("You've been yash rolled", "color2 margin", 0);
      yesu();
      break;
    case "nihal":
      addLine("You've been nihal rolled", "color2 margin", 0);
      annoy();
      break;
    case "hehe":
      loopLines(prashith, "color2 margin", 80);
      break;
    case "gas":
      loopLines(rishi, "color2 margin", 80);
      break;

    case "members":
      addLine("Fetching members list...", "system", 0);
      fetch('/team/terminal-members/')
        .then(response => response.json())
        .then(data => {
          addLine("=== PROTON MEMBERS ===", "color2", 80);
          data.members.forEach((member, index) => {
            const paddedName = member.name.padEnd(30, ' '); // Pad name for alignment
            addLine(`${paddedName}${member.role}`, "color2", 80 * (index + 1));
          });
          addLine("=====================", "color2", 80 * (data.members.length + 1));
        })
        .catch(error => {
          addLine(error, "Error fetching members list", 0);
        });
      break;

    case "socialmedia":
      loopLines(socialmedia, "color2 margin", 80);
      break;
    case "contact":
      const emailUrl = isMobile ? 
        `mailto:proton.cybsec@nmamit.in` :
        `https://mail.google.com/mail/?view=cm&fs=1&to=proton.cybsec@nmamit.in`;
      addLine(`Opening ${isMobile ? 'email app' : 'Gmail compose'}...`, "system", 0);
      setTimeout(() => {
        window.open(emailUrl, '_blank');
        addLine(`If nothing happened, please email us at: proton.cybsec@nmamit.in`, "color2", 80);
      }, 500);
      break;
    case "clear":
      setTimeout(function() {
        terminal.innerHTML = '<a id="before"></a>';
        before = document.getElementById("before");
      }, 1);
      break;
    case "home":
      loopLines(home, "", 80);
      break;
    case "login":
      if (window.isAuthenticated) {
        addLine("Error: You are already logged in as " + currentUser, "error", 0);
        addLine("Use 'logout' command to log out first", "system", 0);
      } else {
        loginStep = 0;
        login();
      }
      break;
    case "gui":
      addLine("Opening GUI-INTERFACE...", "color2", 0);
      newTab(GUI);
      break;
    case "logout":
      fetch('/accounts/logout/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCSRFToken(),
        },
        credentials: 'same-origin'
      })
      .then(response => {
        if (response.ok) {
          currentUser = 'user'; // Reset username to default after logout
          window.isAuthenticated = false;
          updatePrompt('user'); // Reset prompt to default
          addLine("Logout successful! Redirecting to fresh terminal...", "success", 0);
          setTimeout(() => {
            window.location.href = '/';
          }, 1500);
        } else {
          addLine("Logout failed. Please try again.", "error", 0);
        }
      })
      .catch(error => {
        console.error('Logout error:', error);
        addLine("Logout failed: Network or server error", "error", 0);
      });
      break;
    case "echo":
      const matches = fullCommand.match(/echo\s+"([^"]+)"/);
      if (matches && matches[1]) {
        addLine(matches[1], "color2", 0);
      } else {
        addLine('Usage: echo "your message in quotes"', "system", 0);
      }
      break;
    case "get":
      if (parts.length < 2) {
        addLine("Usage: get <member_name>", "system", 0);
        return;
      }
      const memberName = parts.slice(1).join(' ');
      addLine(`Fetching info for ${memberName}...`, "system", 0);
      
      fetch(`/team/get/${encodeURIComponent(memberName)}/`)
        .then(response => response.json())
        .then(data => {
          if (data.success) {
            const emailUrl = isMobile ? 
              `mailto:${data.data.email}` :
              `https://mail.google.com/mail/?view=cm&fs=1&to=${data.data.email}`;
            
            addLine("=== Member Information ===", "color2", 80);
            addLine(`Name: ${data.data.name}`, "color2", 160);
            addLine(`Role: ${data.data.role}`, "color2", 240);
            addLine(`Email: <a href="${emailUrl}" target="_blank">${data.data.email}</a>`, "color2", 320);
            addLine("Social Links:", "color2", 400);
            addLine(`  LinkedIn: <a href="${data.data.linkedin}" target="_blank">[LinkedIn]</a>`, "color2", 480);
            addLine(`  GitHub: <a href="${data.data.github}" target="_blank">[GitHub]</a>`, "color2", 560);
            addLine(`  Instagram: <a href="${data.data.instagram}" target="_blank">[Instagram]</a>`, "color2", 640);
            addLine("=====================", "color2", 720);
          } else {
            addLine(data.message, "error", 0);
          }
        })
        .catch(error => {
          addLine("Error fetching member information", "error", 0);
        });
      break;
    default:
      addLine("<span class=\"inherit\">Command not found. For a list of commands, type <span class=\"command\">'help'</span>.</span>", "error", 100);
      break;
  }
}

function handleLoginInput(input) {
  if (window.isAuthenticated) {
    addLine("Error: You are already logged in", "error", 0);
    loginStep = 0;
    return;
  }
  if (!isPasswordInput) {
    // First input is username
    loginCredentials.username = input.trim();
    isPasswordInput = true;
    addLine("Enter password:", "system", 0);
    command.innerHTML = "";
    return;
  }

  // Second input is password
  loginCredentials.password = tempPassword;
  isPasswordInput = false;
  tempPassword = '';

  fetch('/terminal_login/', {  // Updated endpoint to match urls.py
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',  // Changed to JSON
      'X-CSRFToken': getCSRFToken(),
      'Accept': 'application/json'
    },
    credentials: 'same-origin',
    body: JSON.stringify({
      username: loginCredentials.username,
      password: loginCredentials.password
    })
  })
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      currentUser = loginCredentials.username; // Set the current username after successful login
      loginStep = 0; // Reset login step to exit login mode
      window.username = loginCredentials.username; // Update the global username
      window.isAuthenticated = true;
      updatePrompt(loginCredentials.username); // Update the prompt with the new username
      addLine(`Login successful! Welcome ${loginCredentials.username}`, "success", 0);
      addLine("Type 'help' for available commands", "system", 0);
    } else {
      addLine(`Login failed: ${data.message}`, "error", 0);
      loginStep = 0; // Reset login step on failure
    }
  })
  .catch(error => {
    console.error('Login error:', error);
    addLine("Login failed: Network or server error", "error", 0);
    loginStep = 0; // Reset login step on error
  });
}

function login() {
  if (window.isAuthenticated) {
    addLine("Error: You are already logged in as " + currentUser, "error", 0);
    return;
  }
  loginStep = 1; // Set login mode
  isPasswordInput = false;
  tempPassword = '';
  addLine("=== Terminal Login ===", "system", 0);
  addLine("Enter username:", "system", 0);
}

function getCSRFToken() {
    const csrfCookie = document.cookie.split(';')
        .find(cookie => cookie.trim().startsWith('csrftoken='));
    if (csrfCookie) {
        return csrfCookie.split('=')[1];
    }
    // Fallback to meta tag
    const csrfElement = document.querySelector('[name=csrfmiddlewaretoken]');
    return csrfElement ? csrfElement.value : '';
}

function newTab(link) {
  setTimeout(function() {
    window.open(link, "_blank");
  }, 500);
}

function addLine(text, style, time) {
  var t = "";
  for (let i = 0; i < text.length; i++) {
    if (text.charAt(i) == " " && text.charAt(i + 1) == " ") {
      t += "&nbsp;&nbsp;";
      i++;
    } else {
      t += text.charAt(i);
    }
  }
  setTimeout(function() {
    var next = document.createElement("p");
    next.innerHTML = t;
    next.className = style;

    before.parentNode.insertBefore(next, before);

    window.scrollTo(0, document.body.offsetHeight);
  }, time);
}

function loopLines(name, style, time) {
  name.forEach(function(item, index) {
    addLine(item, style, index * time);
  });
}

// Add this function to update the prompt
function updatePrompt(username) {
    const liner = document.getElementById("liner");
    liner.setAttribute('data-prompt', `${username}@proton:~$ `);
}

// Add this at the end of the file to set initial prompt
document.addEventListener('DOMContentLoaded', function() {
    // Set initial prompt based on authenticated user
    updatePrompt(window.username || 'user');
    // Remove updateEmailUrl call since we're using dynamic function
});

// Ensure textarea stays focused
document.addEventListener('click', function() {
  textarea.focus();
});


