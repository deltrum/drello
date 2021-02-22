<template>
    <div class="task-column" :id="taskColumn.id">
        <header class="task-column__header" :style="{ backgroundColor: taskColumn.color }">
            <h2 class="task-column__title">
                {{taskColumn.title}}
            </h2>
            <span class="task-column__counter">
                ({{tasks.length}})
            </span>
        </header>
        <div class="task-column__content">

            <ul class="task-column__list">

                <li class="task-column__item" v-for="task in tasks" :key="task.id">
                    <button class="task-column__item-del-btn" @click="deleteTask(task.id)">
                        <svg xmlns="http://www.w3.org/2000/svg" width="30.264" height="30.264" viewBox="0 0 30.264 30.264">
                            <path id="plus" d="M28.751,13.619H16.645V1.513a1.513,1.513,0,0,0-3.026,0V13.619H1.513a1.513,1.513,0,0,0,0,3.026H13.619V28.751a1.513,1.513,0,1,0,3.026,0V16.645H28.751a1.513,1.513,0,1,0,0-3.026Zm0,0" transform="translate(0)"/>
                        </svg>
                    </button>
                    <div class="task-column__item-id">
                        id: {{task.id}}
                    </div>
                    <p class="task-column__item-text">
                        {{task.content}}
                    </p>
                </li>

            </ul>

            <button class="task-column__btn" @click="toggleForm()">
                <svg xmlns="http://www.w3.org/2000/svg" width="30.264" height="30.264" viewBox="0 0 30.264 30.264">
                    <path id="plus" d="M28.751,13.619H16.645V1.513a1.513,1.513,0,0,0-3.026,0V13.619H1.513a1.513,1.513,0,0,0,0,3.026H13.619V28.751a1.513,1.513,0,1,0,3.026,0V16.645H28.751a1.513,1.513,0,1,0,0-3.026Zm0,0" transform="translate(0)"/>
                </svg>
                Add a new task
            </button>

            <form class="task-column__item-form" @submit.prevent="addNewTask()">
                <textarea class="task-column__item-text-area" placeholder="Content..." required v-model="newTask.content">
                </textarea>
                <button class="task-column__item-submit submit-btn" type="submit">
                    Submit
                </button>
                <button class="task-column__item-submit submit-btn" @click="toggleForm()">
                    Cancel
                </button>
            </form>
        </div>
    </div>
</template>

<script lang="ts">
    import { AxiosResponse } from 'axios'
    import {ref, reactive, onMounted} from 'vue'
    import {useStore} from 'vuex'

    interface ColumnTask {
        id: number;
        content: string;
        attachment: number;
        owner: number;
    }

    type AppProps = {
        taskColumn: ColumnTask;
    }

    export default {
        name: "TaskColumn",
        props: {
            taskColumn: {} as object,
        },

        setup(props: AppProps){
            const store = useStore()
            const tasks = ref([] as Array<ColumnTask>)
            const newTask = reactive({
                content: '' as string,
                attachment: props.taskColumn.id as number,
            } as ColumnTask)

        
            async function fetchTasks(){
                await store.dispatch('todos/fetchTasks', props.taskColumn.id)
                .then((res: AxiosResponse) => {
                    if(res.status == 200){
                        tasks.value = res.data
                    }
                })
                .catch((err: AxiosResponse) => {
                    console.log(err)
                })
            }

            function toggleForm(){
                const form = document.getElementById('' + props.taskColumn.id)
                if(form){
                    form.classList.toggle('task-column--form-open')
                }
            }

            async function addNewTask(){
                await store.dispatch('todos/addTask', newTask)
                .then((res: AxiosResponse) => {
                    newTask.content = '' 
                    if(res.status == 201){
                        tasks.value.push(res.data)
                    }
                })
                .catch((err: AxiosResponse) => {
                    console.log(err)
                })
            }

            
            async function deleteTask(taskId: number){
                await store.dispatch('todos/deleteTask', {taskId: taskId, columnId: props.taskColumn.id})
                .then((res: AxiosResponse) => {
                    if(res.status == 200){
                        fetchTasks()
                    }
                })
                .catch((err: AxiosResponse) => {
                    console.log(err)
                })
            }

            onMounted(() => {
                fetchTasks()
            })

            return{
                tasks,
                newTask,
                toggleForm,
                addNewTask,
                deleteTask,
            }
        }
    }
</script>
