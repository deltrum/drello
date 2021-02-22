<template>
    <main class="main">
        <div class="container">
            <div class="main__inner">
                <form class="login form" @submit.prevent="onLoginSubmit()">
                    <label class="form__label">
                        Login:
                        <input type="text" class="form__input" placeholder="Login" required v-model="loginData.username">
                    </label>
                    <label class="form__label">
                        Password:
                        <input type="password" class="form__input" placeholder="Password" required v-model="loginData.password">
                    </label>
                    <p class="form__warning" v-if="errorMsg">
                        {{errorMsg}}
                    </p>
                    <button class="form__submit submit-btn" type="submit">
                        Login
                    </button>
                    <router-link class="form__link" :to="{name: 'Register'}">
                        Don't have an account yet?
                    </router-link>
                </form>
            </div>
        </div>
    </main>
</template>


<script lang="ts">
    import { AxiosError, AxiosResponse } from 'axios'
    import {ref, reactive} from 'vue'
    import {useStore} from 'vuex'
    import {useRouter} from 'vue-router'

    export default {
        name: "Login",

        setup(){
            const store = useStore()
            const router = useRouter()
            const errorMsg = ref('' as string)
            const loginData = reactive({
                username: "" as string,
                password: "" as string
            }as object ) 


            async function onLoginSubmit(){
                await store.dispatch('users/login', loginData)
                .then((res: AxiosResponse) => {
                    if(res.status == 200){
                        router.push({ name: "Home"})
                    }
                })
                .catch((err: AxiosError) => {
                    console.log(err)
                    errorMsg.value = err.message
                })
            }

            return{
                errorMsg,
                loginData,
                onLoginSubmit,
            }
        }
    }
</script>
