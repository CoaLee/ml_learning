$(document).ready(function () {
    $('#button_train').on('click', function() {
        $.ajax({
            url: 'ml/_ajax/train',
            data: {
                train_set_size: $('#num_train_set_size').val(),
                learning_rate: $('#num_learning_rate').val(),
                train_steps: $('#num_train_steps').val(),
                batch_test_set_size: $('#num_batch_test_set_size').val()
            },
            success: function(data) {
                var $img_weights_map = $('<img />').attr('src', data.src_weights_map);
                $('#wrapper_weights_map').append($img_weights_map);
            }
        });
    });
});
