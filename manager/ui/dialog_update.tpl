<%inherit file="dialog.tpl"/>

<%block name="blkDialogId">diaUpdate</%block>

<%block name="blkDialogHeader">
  Update Application
</%block>

<%block name="blkDialogContent">
  <form action="" id="appUpdateForm">

    <input type="hidden" name="app" value="${app}">

    <div class="dialog-text">Overwrite engine modules:</div>

    % for module in modulesAll:
      <div class="dialog-text" title="Select this module for updating">
        <input type="checkbox" name="module" value="${module}" ${'checked' if module in modulesUpdated else ''} class="netcheckbox">
        ${module}
      </div>
    % endfor

    <hr>

    <div class="dialog-text" id="updateFileListInfo">Merge/overwrite template-based files (with automatic backup):</div>

    % for file in files:
      <div class="dialog-text" title="Select this template-based file/dir for updating">
       <input type="checkbox" name="file" value="${file}" checked class="appcheckbox">
        <span>${file}</span>
      </div>
    % endfor

    <input type="submit" id="updateApp" value="Update App" class="button update">
  </form>
</%block>

<%block name="blkDialogScript">
  diaUpdateClose.addEventListener('click', function() {
      destroyDialog('diaUpdate');
  });

  appUpdateForm.addEventListener('submit', function(event) {
      var formData = new FormData(appUpdateForm);

      makeRequest('/update_app/', formData, function(response) {
          destroyDialog('diaUpdate');

          var dia = appendDialog(response);
          openDialog(dia);
      });

      event.preventDefault();
  });

  focusElem('updateApp');
</%block>
