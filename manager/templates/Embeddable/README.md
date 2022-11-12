# Verge3D React.js Application Example

1) Create a React.js application via the Create React App utility:

    ```
    npx create-react-app react-v3d-app
    ```

2) Copy the following files from Verge3D distribution into your app:

    * the contents of Verge3D's `manager/templates/Embeddable/public` directory
    to `react-v3d-app/public`

    * the contents of Verge3D's `manager/templates/Embeddable/src` directory to
    `react-v3d-app/src`

    * the Verge3D engine file `build/v3d.js` to `react-v3d-app/public`

    or use the commands below:

    <u>Linux/macOS</u>

    *Change `V3D_PATH` and `MY_PATH` to where the Verge3D distribution and your
    React application are located respectively.*

    ```sh
    V3D_PATH=path/to/v3d/distribution
    MY_PATH=path/to/my/react/app
    cp -r $V3D_PATH/manager/templates/Embeddable/public/* $MY_PATH/public/
    cp -r $V3D_PATH/manager/templates/Embeddable/src/* $MY_PATH/src/
    cp $V3D_PATH/build/v3d.js $MY_PATH/public/
    ```

    <u>Windows(PowerShell)</u>

    *Change `V3D_PATH` and `MY_PATH` to where the Verge3D distribution and your
    React application are located respectively.*

    ```powershell
    $V3D_PATH = "path\to\v3d\distribution"
    $MY_PATH = "path\to\my\react\app"
    Copy-Item -Path "$V3D_PATH\manager\templates\Embeddable\public\*" -Destination "$MY_PATH\public" -Recurse
    Copy-Item -Path "$V3D_PATH\manager\templates\Embeddable\src\*" -Destination "$MY_PATH\src" -Recurse
    Copy-Item "$V3D_PATH\build\v3d.js" -Destination "$MY_PATH\public"
    ```

3) Add the following script tag into `react-v3d-app/public/index.html`:

    ```html
    <script src="%PUBLIC_URL%/v3d.js"></script>
    ```

4) Create a file called `react-v3d-app/src/V3DApp.js` with the following content:

    ```js
    import React from 'react';

    import * as v3dAppAPI from './v3dApp/app';
    import './v3dApp/app.css';

    class V3DApp extends React.Component {

      #app = null;

      componentDidMount() {
        v3dAppAPI.createApp().then(app => {
          this.#app = app;
        });
      }

      componentWillUnmount() {
        if (this.#app !== null) {
          this.#app.dispose();
          this.#app = null;
        }
      }

      render() {
        return <div id={v3dAppAPI.CONTAINER_ID}>
          <div id="fullscreen_button" className="fullscreen-button fullscreen-open" title="Toggle fullscreen mode"></div>
        </div>;
      }
    }

    export default V3DApp;
    ```

5) Replace the contents of `react-v3d-app/src/index.js` with the following code:

    ```js
    import React from 'react';
    import ReactDOM from 'react-dom/client';

    import V3DApp from './V3DApp';

    const root = ReactDOM.createRoot(document.getElementById('root'));
    root.render(<V3DApp/>);
    ```

6) Run the development server by executing the following command in the
`react-v3d-app` directory:

    ```
    npm start
    ```

    By default the application now should be available at http://localhost:3000/.


# Verge3D Vue.js Application Example

1) Create a Vue.js application via the Vue CLI utility:

    ```
    npx @vue/cli create vue-v3d-app
    ```

2) Copy the following files from Verge3D distribution into your app:

    * the contents of Verge3D's `manager/templates/Embeddable/public` directory
    to `vue-v3d-app/public`

    * the contents of Verge3D's `manager/templates/Embeddable/src` directory to
    `vue-v3d-app/src`

    * the Verge3D engine file `build/v3d.js` to `vue-v3d-app/public`

    or use the commands below:

    <u>Linux/macOS</u>

    *Change `V3D_PATH` and `MY_PATH` to where the Verge3D distribution and your
    Vue application are located respectively.*

    ```sh
    V3D_PATH=path/to/v3d/distribution
    MY_PATH=path/to/my/vue/app
    cp -r $V3D_PATH/manager/templates/Embeddable/public/* $MY_PATH/public/
    cp -r $V3D_PATH/manager/templates/Embeddable/src/* $MY_PATH/src/
    cp $V3D_PATH/build/v3d.js $MY_PATH/public/
    ```

    <u>Windows(PowerShell)</u>

    *Change `V3D_PATH` and `MY_PATH` to where the Verge3D distribution and your
    Vue application are located respectively.*

    ```powershell
    $V3D_PATH = "path\to\v3d\distribution"
    $MY_PATH = "path\to\my\vue\app"
    Copy-Item -Path "$V3D_PATH\manager\templates\Embeddable\public\*" -Destination "$MY_PATH\public" -Recurse
    Copy-Item -Path "$V3D_PATH\manager\templates\Embeddable\src\*" -Destination "$MY_PATH\src" -Recurse
    Copy-Item "$V3D_PATH\build\v3d.js" -Destination "$MY_PATH\public"
    ```

3) Add the following script tag into `vue-v3d-app/public/index.html`:

    ```html
    <script src="<%= BASE_URL %>v3d.js"></script>
    ```

4) Create a file `vue-v3d-app/src/components/V3DApp.vue` containing the following
code:

    <u>Vue 2</u>

    ```js
    <template>
      <div :id="containerId">
        <div id="fullscreen_button" class="fullscreen-button fullscreen-open" title="Toggle fullscreen mode"></div>
      </div>
    </template>

    <script>
    import * as v3dAppAPI from '../v3dApp/app';

    export default {
      name: 'V3DApp',

      data() {
        return {
          containerId: v3dAppAPI.CONTAINER_ID,
        };
      },

      app: null,

      mounted() {
        v3dAppAPI.createApp().then(app => {
          this.$options.app = app;
        });
      },

      beforeDestroy() {
        if (this.$options.app) {
          this.$options.app.dispose();
          this.$options.app = null;
        }
      },
    }
    </script>

    <style>
    @import '../v3dApp/app.css';
    </style>
    ```

    <u>Vue 3</u>

    ```js
    <template>
      <div :id="containerId">
        <div id="fullscreen_button" class="fullscreen-button fullscreen-open" title="Toggle fullscreen mode"></div>
      </div>
    </template>

    <script>
    import * as v3dAppAPI from '../v3dApp/app';

    export default {
      name: 'V3DApp',

      data() {
        return {
          containerId: v3dAppAPI.CONTAINER_ID,
        };
      },

      app: null,

      mounted() {
        v3dAppAPI.createApp().then(app => {
          this.$options.app = app;
        });
      },

      beforeUnmount() {
        if (this.$options.app) {
          this.$options.app.dispose();
          this.$options.app = null;
        }
      },
    }
    </script>

    <style>
    @import '../v3dApp/app.css';
    </style>
    ```

5) Replace the contents of `vue-v3d-app/src/App.vue` with the following code:

    ```js
    <template>
      <V3DApp></V3DApp>
    </template>

    <script>
    import V3DApp from './components/V3DApp.vue';

    export default {
      name: 'App',
      components: {
        V3DApp,
      },
    }
    </script>
    ```

6) Run the development server by executing the following command in the
`vue-v3d-app` directory:

    ```
    npm run serve
    ```

    By default the application now should be available at http://localhost:8080/.
