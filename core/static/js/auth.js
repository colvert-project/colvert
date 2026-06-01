(function () {
  function getCookie(name) {
    var value = '; ' + document.cookie;
    var parts = value.split('; ' + name + '=');
    if (parts.length === 2) {
      return parts.pop().split(';').shift();
    }
    return '';
  }

  function setAlert(message) {
    var alertEl = document.getElementById('signin-alert');
    if (!alertEl) {
      return;
    }
    if (message) {
      alertEl.textContent = message;
      alertEl.classList.remove('d-none');
    } else {
      alertEl.textContent = '';
      alertEl.classList.add('d-none');
    }
  }

  function resetFieldErrors(form) {
    var invalidFields = form.querySelectorAll('.is-invalid');
    invalidFields.forEach(function (field) {
      field.classList.remove('is-invalid');
    });
  }

  function applyFieldErrors(form, errors) {
    if (!errors) {
      return;
    }

    Object.keys(errors).forEach(function (fieldName) {
      var field = form.querySelector('[name="' + fieldName + '"]');
      if (field) {
        field.classList.add('is-invalid');
      }
    });
  }

  function bindSigninForm(form) {
    if (!window.fetch || !window.FormData) {
      return;
    }

    form.addEventListener('submit', function (event) {
      event.preventDefault();
      resetFieldErrors(form);
      setAlert('');

      fetch(form.dataset.apiEndpoint, {
        method: 'POST',
        headers: {
          'X-CSRFToken': getCookie('csrftoken'),
          'X-Requested-With': 'XMLHttpRequest'
        },
        body: new FormData(form),
        credentials: 'same-origin'
      })
        .then(function (response) {
          return response.json().then(function (data) {
            return { status: response.status, data: data };
          });
        })
        .then(function (result) {
          if (result.status >= 200 && result.status < 300 && result.data.redirect_url) {
            window.location.assign(result.data.redirect_url);
            return;
          }

          applyFieldErrors(form, result.data.errors);
          setAlert(result.data.message || 'Authentication failed.');
        })
        .catch(function () {
          setAlert('Network error. Please retry.');
        });
    });
  }

  function bindLogoutForm(form) {
    if (!window.fetch || !window.FormData) {
      return;
    }

    form.addEventListener('submit', function (event) {
      event.preventDefault();

      fetch(form.dataset.apiEndpoint, {
        method: 'POST',
        headers: {
          'X-CSRFToken': getCookie('csrftoken'),
          'X-Requested-With': 'XMLHttpRequest'
        },
        body: new FormData(form),
        credentials: 'same-origin'
      })
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          window.location.assign(data.redirect_url || '/signin/');
        })
        .catch(function () {
          form.submit();
        });
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    var signinForm = document.getElementById('signin-form');
    if (signinForm && signinForm.dataset.apiEndpoint) {
      bindSigninForm(signinForm);
    }

    var logoutForms = document.querySelectorAll('form[data-ajax-auth="logout-form"]');
    logoutForms.forEach(function (form) {
      if (form.dataset.apiEndpoint) {
        bindLogoutForm(form);
      }
    });
  });
})();
