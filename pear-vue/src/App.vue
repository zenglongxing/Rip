<template>
    <a-locale-provider :locale="locale">
        <div id="app">
            <router-view/>
        </div>
    </a-locale-provider>
</template>

<script>
    import zhCN from 'ant-design-vue/lib/locale-provider/zh_CN'
    import enquireScreen from '@/utils/device'

    export default {
        name: 'App',
        data() {
            return {
                locale: zhCN,
            }
        }
    }
</script>

<style>
    #app {
        height: 100%;
    }
</style>
