<template>
    <main class="home main">
        <div class="container">
            <div class="home__inner">
                <div class="home__rows">
                    <TaskColumn v-for="taskColumn in taskColumns" :key="taskColumn.id" v-bind="{taskColumn: taskColumn}"/>
                </div>
            </div>
        </div>
    </main>
</template>

<script lang="ts">
    import { Options, Vue } from 'vue-class-component'
    import TaskColumn from '@/components/TaskColumn.vue';
    import { AxiosResponse } from 'axios';

    @Options({
        name: "Home",
        components: {
            TaskColumn,
        },
    })
    export default class Home extends Vue {

        get taskColumns(){
            return this.$store.getters['todos/getTaskColumns']
        }

        async fetchTaskColums(){
            await this.$store.dispatch('todos/fetchTaskColumns')
            .catch((err: AxiosResponse) => {
                console.log(err)
            })
        }

        mounted(){
            this.fetchTaskColums()
        }

    }
</script>
