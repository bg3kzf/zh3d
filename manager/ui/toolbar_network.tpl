% if len(filesViewInfo):
  <div class="toolbar-network">
    <a href="javascript:void(0);" onclick=downloadNetworkFiles() class="toolbar-network-icon toolbar-network-icon-download" title="Download selected files"></a>
    <a href="javascript:void(0);" onclick=removeS3Files() class="toolbar-network-icon toolbar-network-icon-delete" title="Delete selected files"></a>
  </div>
% endif
