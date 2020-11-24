function add_this(){
    var save_list = $.cookie('save_list');
    if (save_list == null){
        save_list = "";
    }

    save_list += ','+$('#id').text();
    $.cookie('save_list', save_list,{ expires: 7, path: '/' });
    refresh_savelist()
    toastr.options.positionClass = "toast-top-center";
    refresh_btn_add()
    toastr.success('Success.')
    console.log(save_list)
}
function clear_all(){
    $.cookie('save_list', '',{ expires: 7, path: '/' });
    refresh_savelist()
    toastr.options.positionClass = "toast-top-center";
    refresh_btn_add()
    toastr.success('Success.')
}
function refresh_savelist(){
    $.ajax(
        {
            url: "/get_savelist",
            success: function (result) {
                $("#savelist").html(result);
                $("#count_savelist").text($("#count").text())
               }
        });
}
function refresh_btn_add(){
    let id = $('#id').text();
        $.ajax(
        {
            url: "/check_added",
            data: "id=" + id,
            success: function (result) {
                $("#btnAdd").html(result);
            }
        });
}
$("#savelistDropdown").click(refresh_savelist)
// when the page is load refresh the save list.
$( document ).ready(function() {
    refresh_savelist();
    refresh_btn_add();
});