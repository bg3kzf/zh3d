<html>
<head>
  <title>三维可视化项目商店</title>
  <%include file="head.tpl"/>
</head>

<body>
  <div class="main-panel">

    <div class="banner banner-store"></div>

    <%include file="search.tpl"/>

    <table class="asset-store">
      <thead>
        <tr>
          <th>item</th>
          <th>description</th>
        </tr>
      </thead>

      <tbody>
        % for demo in sorted(demos, key=lambda elem: elem['title']):
          % if demo['package'] == package.lower() or package == 'ALL':
          <tr class="filterable" id="${demo['title'].lower().replace(' ', '_')}">
            <td class="asset-store-item">
              <div class="margin: 10px">
                <a href="${demo['buy_url'] if 'buy_url' in demo else demo['exec_url']}" target="_blank">
                  <img src="${demo['cover_image']}" width="1200" height="630" class="asset-store-image">
                </a>
                <div class="asset-store-item-bar">
                  <div class="asset-store-icon-${demo['package'].lower()}" title="This asset is compatible with ${demo['package'].title()}"></div>
                  <span class="asset-store-item-title">${demo['title']}</span>
                  <span class="asset-store-item-type">${demo['type'].title()}</span>
                  <div class="asset-store-icon-price"><span class="asset-store-item-price">${demo['price'].title()}</span></div>
                </div>
              </div>
            </td>
            <td class="asset-store-item">
              <div>${demo['description']}</div>
              <div class="asset-store-item-spacing"></div>
              <div class="asset-store-icons-invisible-bar">
                % if 'buy_url' in demo:
                  <a href="${demo['buy_url']}" target="_blank" class="asset-store-icon-buy" title="Buy"></a>
                % else:
                  <a href="${demo['exec_url']}" target="_blank" class="asset-store-icon-run" title="Run"></a>
                  <a href="javascript:void(0);" onclick=downloadDemo("${demo['download_url'] | u}") class="asset-store-icon-download" title="Download"></a>
                % endif
              </div>
            </td>
          </tr>
          % endif
        % endfor
      </tbody>
      <tfoot><tr><td colspan=2>© DX LLC</td></tr></tfoot>
    </table>

  </div>

  <%include file="toolbar.tpl"/>
  <%include file="toolbar_store.tpl"/>
  <%include file="dialog_store_download.tpl"/>

</body>
</html>
