
import { createStore, createLogger } from 'vuex'
import {todos} from './modules/todos'
import {users} from './modules/users'


export default createStore({
    modules: {
        todos,
        users,
    },
    plugins: [createLogger()],
})