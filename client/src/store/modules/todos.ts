
import { GetterTree, ActionTree, MutationTree} from 'vuex'
import axios from 'axios'

interface TaskColumn {
    id: number;
    title: string;
    color: string;
}

interface DeleteDataIds {
    columnId: number;
    taskId: number;
}

const state = () => ({
    taskColumns: [] as Array<TaskColumn>,
})

type RootState = ReturnType<typeof state>

const getters: GetterTree<RootState, RootState> = {
    getTaskColumns(state) {
        return state.taskColumns
    },
}

const mutations: MutationTree<RootState> = {
    mAddTaskColumns(state, data: Array<TaskColumn>) {
        state.taskColumns = data
    },
}

const actions: ActionTree<RootState, RootState> = {
    async fetchTaskColumns({ commit }) {
        return new Promise((resolve, reject) => {
            axios.get(process.env.VUE_APP_BASE_URL + '/todos/api/taskcolumns/')
            .then((response) => {
                commit('mAddTaskColumns', response.data)
                resolve(response)
            })
            .catch((err) => {
                reject(err)
            })
        })
    },

    async fetchTasks(_, columnId: number) {
        return new Promise((resolve, reject) => {
            axios.defaults.headers.common["Authorization"] =
            "token " + localStorage.getItem('user_token');
            axios.get(process.env.VUE_APP_BASE_URL + `/todos/api/tasks/${columnId}/`)
            .then((response) => {
                resolve(response)
            })
            .catch((err) => {
                reject(err)
            })
        })
    },

    async addTask(_, newTask: object) {
        return new Promise((resolve, reject) => {
            axios.defaults.headers.common["Authorization"] =
            "token " + localStorage.getItem('user_token');
            axios.post(process.env.VUE_APP_BASE_URL +  `/todos/api/task/`, newTask)
            .then((res) => {
                resolve(res);
            })
            .catch((err) => {
                reject(err)
            })
        })
    },

    async deleteTask(_, dataIds: DeleteDataIds) {
        return new Promise((resolve, reject) => {
            axios.delete(process.env.VUE_APP_BASE_URL +  `/todos/api/task/${dataIds.taskId}/`)
            .then((res) => {
                resolve(res);
            })
            .catch((err) => {
                reject(err)
            })
        })
    },
}

export const todos ={
    namespaced: true,
    state,
    getters,
    mutations,
    actions,
}