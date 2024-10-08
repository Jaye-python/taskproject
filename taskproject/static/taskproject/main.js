
function showPasswordLogin() {
    $('#togglePasswordLogin').on('click', function() {
      var passwordField = $('#id_password');
      var type = passwordField.attr('type') === 'password' ? 'text' : 'password';
      passwordField.attr('type', type);

      $(this).toggleClass('bi bi-eye-slash-fill');
      $(this).toggleClass('bi bi-eye-fill');
    });
  };

  function showPassword() {
    $('#togglePassword').on('click', function() {
      var passwordField = $('#id_password1');
      var type = passwordField.attr('type') === 'password' ? 'text' : 'password';
      passwordField.attr('type', type);

      $(this).toggleClass('bi bi-eye-slash-fill');
      $(this).toggleClass('bi bi-eye-fill');
    });
  };

  function showPassword2() {
    $('#togglePassword2').on('click', function() {
      var passwordField = $('#id_password2');
      var type = passwordField.attr('type') === 'password' ? 'text' : 'password';
      passwordField.attr('type', type);

      $(this).toggleClass('bi bi-eye-slash-fill');
      $(this).toggleClass('bi bi-eye-fill');

    });
  };


function AjaxTaskLoading() {
    $('#load-in-progress').click(function() {
        loadTasks('/tasks/in_progress/');
    });
    $('#load-completed').click(function() {
        loadTasks('/tasks/completed/');
    });
    $('#load-overdue').click(function() {
        loadTasks('/tasks/overdue/');
    });

    function loadTasks(url) {
        $.ajax({
            url: url,
            method: 'GET',
            success: function(response) {
                var data = response.results;
                var dataCount = data.length

                $('.task-container').empty();
                if (Array.isArray(data) && data.length > 0) {
                    data.forEach(function(task) {

                        let taskHtml = `
                        <div class="p-4 bg-white rounded-md rounded-md border border-blue-600 shadow-sm mb-4">
                        <h2 class="font-bold">${task.status} <span class="text-gray-500">(${ dataCount})</span></h2>
                    </div>
                            <div class="p-4 bg-white rounded-md shadow-sm">
                                <div class="flex justify-between items-center">
                                    <div class="flex items-center space-x-2">
                                        <span class="text-dark-500">
                                            <button class="p-2 bg-gray-300 rounded-md">${task.priority}</button>
                                        </span>
                                        <span class="text-blue-500">
                                            <button class="p-2 shadow bg-white rounded-md">
                                                <i class="bi bi-alarm"></i> ${new Date(task.due_date).toLocaleDateString()}
                                            </button>
                                        </span>
                                        <span class="text-blue-600">
                                            <button class="p-2 bg-blue-100 rounded-md">${task.title}</button>
                                        </span>
                                    </div>
                                    <button class="text-gray-500">...</button>
                                </div>
                                <br>
                                <div class="p-4 bg-gray-100 rounded-md shadow-sm mb-4">
                                    <h2 class="font-bold">User Flow</h2>
                                    <p class="text-gray-500">${task.description}</p>
                                    <div class="flex items-center justify-between mt-4">

                                        <div class="flex items-center space-x-2">
                                            <a href="/task-detail/${task.id}/">
                                                <button class="text-blue-500"><i class="bi bi-eye"></i></button>
                                            </a>
                                            <a href="/delete-task/${task.id}/">
                                                <button class="text-blue-500"><i class="bi bi-trash"></i></button>
                                            </a>
                                            <a href="/update-task/${task.id}/">
                                                <button class="text-blue-500"><i class="bi bi-pencil"></i></button>
                                            </a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        `;
                        $('.task-container').append(taskHtml);
                    });
                } else {
                    $('.task-container').append('<p>No tasks found.</p>');
                }
            },
            error: function(error) {
                $('.task-container').empty().append('<p>Error loading tasks.</p>');
            }
        });
    }
}


function SearchTasks(searchQuery) {
      $.ajax({
          url: '/task/search/',
          method: 'GET',
          data: {
              q: searchQuery
          },
          success: function(response) {
              var data = response.results;
              var dataCount = data.length

              $('.task-container').empty();
              if (Array.isArray(data) && data.length > 0) {
                  data.forEach(function(task) {
                    let taskHtml = `
                        <div class="p-4 bg-white rounded-md rounded-md border border-blue-600 shadow-sm mb-4">
                        <h2 class="font-bold">${task.status}</h2>
                    </div>
                            <div class="p-4 bg-white rounded-md shadow-sm">
                                <div class="flex justify-between items-center">
                                    <div class="flex items-center space-x-2">
                                        <span class="text-dark-500">
                                            <button class="p-2 bg-gray-300 rounded-md">${task.priority}</button>
                                        </span>
                                        <span class="text-blue-500">
                                            <button class="p-2 shadow bg-white rounded-md">
                                                <i class="bi bi-alarm"></i> ${new Date(task.due_date).toLocaleDateString()}
                                            </button>
                                        </span>
                                        <span class="text-blue-600">
                                            <button class="p-2 bg-blue-100 rounded-md">${task.title}</button>
                                        </span>
                                    </div>
                                    <button class="text-gray-500">...</button>
                                </div>
                                <br>
                                <div class="p-4 bg-gray-100 rounded-md shadow-sm mb-4">
                                    <h2 class="font-bold">User Flow</h2>
                                    <p class="text-gray-500">${task.description}</p>
                                    <div class="flex items-center justify-between mt-4">

                                        <div class="flex items-center space-x-2">
                                            <a href="/task-detail/${task.id}/">
                                                <button class="text-blue-500"><i class="bi bi-eye"></i></button>
                                            </a>
                                            <a href="/delete-task/${task.id}/">
                                                <button class="text-blue-500"><i class="bi bi-trash"></i></button>
                                            </a>
                                            <a href="/update-task/${task.id}/">
                                                <button class="text-blue-500"><i class="bi bi-pencil"></i></button>
                                            </a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        `;
                        $('.task-container').append(taskHtml);

                  });
              } else {
                  $('.task-container').append('<p>No tasks found.</p>');
              }
          },
          error: function(error) {
              $('.task-container').empty().append('<p>Error loading tasks.</p>');
          }
      });
  }


function SearchTrigger() {
  $('#search-input').keyup(function() {
      var searchQuery = $(this).val().trim();
      if (searchQuery.length > 0) {
        SearchTasks(searchQuery);
      } else {

          $('#task-container').empty();
      }
  });
};
