// app init
(() => {

  let setFocus = (state) => {
    let $inputName = doc.get('inputName');
    if (state) {
      $inputName.focus();
    } else {
      $inputName.value = '';
    }
  };

  let getProgressPercent = (curr, total) => {
    let delta = (curr / total) * 100 ;
    return {
      width: `${delta}%`
    };
  };

  let vm = new Vue({
    el: '#app',
    data: {
      uploadProgress: {
        width: '0%'
      },
      recognitionProgress: {
        width: '0%'
      },
      isDialogOpened: false,
      isProcessing: false,
      entries: [],
      entry: {}
    },
    created: () => {
      doc.all('.form-group .hide').forEach((el) => {
        el.removeClass('hide');
      });
    },
    methods: {
      startProcess: () => {
        let $fileToReco = doc.get('fileToReco');
        let file = $fileToReco.files[0];
        if (!file) {
          return false;
        }
        vm.isProcessing = true;
        vm.uploadProgress = {
          width: '0%'
        };
        vm.recognitionProgress = {
          width: '0%'
        };
        return vm.upload(file);
      },
      toggleDialog: () => {
        let currState = vm.isDialogOpened;
        let newState = !currState;
        vm.isDialogOpened = newState;

        setTimeout(() => {
          setFocus(newState);
        }, 100);
      },
      upload: (file) => {
        let formData = new FormData();
        formData.append('fileToReco', file);
        let opts = {
          headers: {
            enctype: 'multipart/form-data'
          },
          dataType: 'formdata',
          timeout: 3 * 6e4
        };
        qwest.post('/upload', formData, opts, (xhr) => {
          xhr.upload.onprogress = (e) => {
            let {
              loaded,
              total
            } = e;
            vm.uploadProgress = getProgressPercent(loaded, total);
          };
        }).then((xhr, res) => {
          if (res.error) {
            console.trace(res);
          }
          vm.isProcessing = false;
        }).catch((err) => {
          console.trace(err);
        });
      }
    }
  });

  return vm;
})();