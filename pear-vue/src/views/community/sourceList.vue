<template>
    <div>
        <a-row :gutter="24">
            <a-col :span="6" v-for="(source,index) in sources" :key="source.id">
                <a-card hoverable style="width: 300px" class="star-card">
                    <img
                            slot="cover"
                            :alt="'图片'"
                            :src="source.local_path"
                            :preview="index"
                    />
                    <a-card-meta :title="source.text" :description="source.content">
                    </a-card-meta>
                </a-card>
            </a-col>
        </a-row>
    </div>
</template>

<script>
import {getAction} from "../../api/manage";

export default {
    name: "sourceList",
    data() {
        return {
            sources: []
        }
    },
    created() {
        this.showSource()
    },
    methods: {
        showSource() {
            getAction('/source/', {}).then((res) => {
                if (res.success) {
                    this.sources = res.data
                }
            })
        }
    }
}
</script>

<style scoped>
    .star-card {
        height: 350px;
    }
</style>
