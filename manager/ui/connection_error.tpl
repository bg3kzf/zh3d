<%namespace name="utils" file="utils.tpl"/>

<html>
<head>
  <title>三维可视化项目管理系统</title>
  <%include file="head.tpl"/>

  <script>
    // NOTE: disable slow refresh on Windows
    if (['Win32', 'Win64', 'Windows', 'WinCE'].indexOf(window.navigator.platform) == -1)
      setTimeout(function(){ location.reload(); }, 5000);
  </script>
</head>

<body>
  <div class="main-panel">

    <div class="banner"></div>

    <table class="network-directory">
      <thead>
        <tr>
          <th colspan=2>
            应用编辑器连接错误！
          </th>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td colspan=2>
            <div class="error-message">
              <p>无法连接到服务器，请检查服务是否启动!</p>
              <p>请打开CMD命令窗口至'manager'目录下, 运行'python server.py'</p>
            </div>
          </td>
        </tr>
      </tbody>
      <tfoot><tr><td colspan=2>© DX LLC</td></tr></tfoot>
    </table>

  </div>

</body>
</html>
