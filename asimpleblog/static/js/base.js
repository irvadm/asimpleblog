// Hide success/error messages.
setTimeout(function () {
    $('.message').fadeOut('fast');
}, 2000);


$('#comment-list').on('click', '.delete-comment', function () {
    var li = $(this).closest('li');
    let commentID = $(li).attr('comment-id');
    let csrf = $(li).attr('csrf');
    let url = `/posts/comment/delete/`;
    $.ajax({
        url: url,
        type: 'POST',
        data: {
            'commentID': commentID,
            'csrfmiddlewaretoken': csrf
        },
        success: function (response) {
            console.log('successfully deleted comment!');
            $(li).fadeOut(400, function () {
                $(li).remove();
            });
        }
    });
});

$('#commentCreateForm').submit(function (e) {
    var form = $(this);
    let data = form.serialize();
    let url = '/posts/comment/create/'
    $.ajax({
        url: url,
        type: form.attr('method'),
        data: data,
        success: function (response) {
            $("textarea[name='content']").val('');
            $('#comment-list').html(response)
        }
    });
    return false;
});
