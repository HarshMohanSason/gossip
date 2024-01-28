  // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.2/firebase-app.js";

  import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.7.2/firebase-analytics.js";

  // TODO: Add SDKs for Firebase products that you want to use

  // https://firebase.google.com/docs/web/setup#available-libraries


  // Your web app's Firebase configuration

  // For Firebase JS SDK v7.20.0 and later, measurementId is optional

  const firebaseConfig = {

    apiKey: "AIzaSyCKbdTL5stdNTPl9jnPwThsQZXUtO-KOPg",

    authDomain: "gossip-4cbb8.firebaseapp.com",

    projectId: "gossip-4cbb8",

    storageBucket: "gossip-4cbb8.appspot.com",

    messagingSenderId: "641292463940",

    appId: "1:641292463940:web:b9de1342763f4ed5ea7111",

    measurementId: "G-13QRB4RL2Q"

  };


  // Initialize Firebase

  const app = initializeApp(firebaseConfig);

  const analytics = getAnalytics(app);
