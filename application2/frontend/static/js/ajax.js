// 处理请求的接口
(function () {
    var MyAjax = {
        getxhr: function () {
            return new XMLHttpRequest();
        },
        get: function (url, fun, sync = true) {
            var xhr = this.getxhr();
            xhr.onreadystatechange = function () {
                if (xhr.readyState == 4) {
                    fun(xhr.responseText);
                }
            }
            xhr.open('get', url, sync);
            xhr.send();
        },
        post: function (url, post_data, fun, sync = true) {
            var xhr = this.getxhr;
            xhr.onreadystatechange = function () {
                if (xhr.readyState == 4) {
                    fun(xhr.responseText);
                }
            }
            xhr.open('post', url, sync);
            xhr.send(post_data);
        }
    }
    window.myajax = MyAjax;
})()
