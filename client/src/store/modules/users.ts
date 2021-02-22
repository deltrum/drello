
import {ActionTree} from 'vuex'
import axios from 'axios'


const state = () => ({
})

type RootState = ReturnType<typeof state>


const actions: ActionTree<RootState, RootState> = {

    async login(_, loginData: object) {
        return new Promise((resolve, reject) => {
            axios.post(process.env.VUE_APP_BASE_URL + `/users/api/login/`, loginData)
            .then((response) => {
                resolve(response)
                const token = response.data.token;
                localStorage.setItem("user_token", token);
            })
            .catch((err) => {
                console.log(loginData)
                reject(err)
            })
        })
    },

    logout({getters}) {
        if (getters.isLoggedIn) {
            localStorage.removeItem("user_token");
        }
    },

    async register(_, registerData: object) {
        return new Promise((resolve, reject) => {
            axios.post(process.env.VUE_APP_BASE_URL + `/users/api/register/`, registerData)
            .then((response) => {
                resolve(response)
                const token = response.data.token;
                localStorage.setItem("user_token", token);
            })
            .catch((err) => {
                reject(err)
            })
        })
    },
}

export const users = {
    namespaced: true,
    state,
    actions,
}