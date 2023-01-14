/**
 * Author: Wilson Pilco Nuñez
 * Email: wilsonaux1@gmail.com
 * Created at: 2023-01-12 22:22
 */
import Cookies from "js-cookie";
import http from "src/utils/http.js";

class AuthService {
  static async login(username, password) {
    try {
      var response = await http.post("api/token/", {
        username,
        password
      });
      var data = response.data;
      Cookies.set("token", "Bearer " + data.access);
      Cookies.set("refreshToken", data.refresh);
      return {
        success: true,
        message: ""
      };
    } catch (e) {
      return {
        success: false,
        message: "Error en la autenticacion: " + e.response.data.detail
      };
    } finally {
      //
    }
  }
}

export default AuthService;
