/**
 * Author: Wilson Pilco Nuñez
 * Email: wilsonaux1@gmail.com
 * Created at: 2023-01-12 20:14
 */
import axios from "axios";
import Cookies from "js-cookie";

var sessionToken = Cookies.get("token");
// var refreshToken = Cookies.get('refreshToken');

const http = axios.create({
  baseURL: process.env.VUE_APP_API_URL,
  headers: {
    "Access-Control-Allow-Origin": "*",
    Authorization: sessionToken
  }
});

export default http;
