<template>
    <main class="main">
        <div class="container">
            <div class="main__inner">
                <form class="register form" @submit.prevent="onRegisterSubmit()">
                    <label class="form__label">
                        Login:
                        <input type="text" class="form__input" placeholder="Login" required v-model="registerData.username">
                    </label>
                    <label class="form__label">
                        Email:
                        <input type="email" class="form__input" placeholder="Email" required v-model="registerData.email">
                    </label>
                    <div class="form__group">
                        <label class="form__label">
                            Password:
                            <input type="password" class="form__input" placeholder="Password" required v-model="registerData.password">
                        </label>
                        <label class="form__label">
                            Repeat Password:
                            <input type="password" class="form__input" placeholder="Repeat Password" required v-model="registerData.password2">
                        </label>
                    </div>
                    <p class="form__warning" v-if="errorMsg">
                        {{errorMsg}}
                    </p>
                    <button class="form__submit submit-btn" type="submit">
                        Register
                    </button>
                    <router-link class="form__link" :to="{name: 'Login'}">
                        Have an account already?                        
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

    interface RegisterData{
        username: string;
        email: string;
        password: string;
        password2: string;
    }

    export default {
        name: "Register",

        setup(){
            const store = useStore()
            const router = useRouter()
            const errorMsg = ref('' as string)
            const registerData = reactive({
                username: "" as string,
                email: "" as string,  
                password: "" as string,
                password2: "" as string,
            }as RegisterData ) 

            async function Login(){
                await store.dispatch('users/login', {username: registerData.username, password: registerData.password})
                .then((res: AxiosResponse) => {
                    if(res.status == 200){
                        router.push({ name: "Home"})
                    }
                })
                .catch((err: AxiosResponse) => {
                    console.log(err)
                })
            }

            async function onRegisterSubmit(){
                await store.dispatch('users/register', registerData)
                .then((res: AxiosResponse) => {
                    if(res.status == 200){
                        Login()
                    }
                })
                .catch((err: AxiosError) => {
                    console.log(err)
                    errorMsg.value = err.message
                })
            }

            return{
                errorMsg,
                registerData,
                onRegisterSubmit,
            }
        }
    }
</script>
