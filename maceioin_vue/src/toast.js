import Toast from 'vue-toastification';
import 'vue-toastification/dist/index.css';

const options = {
  position: "top-right",
  timeout: 3000,
  closeOnClick: true,
  pauseOnHover: true,
  draggable: true
};

export default (app) => {
  app.use(Toast, options);
};
