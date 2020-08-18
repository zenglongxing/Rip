<template>
  <a-select :value="arrayValue" 
  :filterOption="filterOption"
   @change="onChange" mode="multiple" :placeholder="placeholder">
    <a-select-option
      v-for="(item,index) in options"
      :key="index"
      :value="item.value">
      {{ item.text || item.label }}
    </a-select-option>
  </a-select>
</template>

<script>
  //option {label:,value:}
  export default {
    name: 'JSelectMultiple',
    props: {
      placeholder:{
        type: String,
        default:'',
        required: false
      },
      value:{
        type: String,
        required: false
      },
      readOnly:{
        type: Boolean,
        required: false,
        default: false
      },
      options:{
        type: Array,
        required: true
      },
      triggerChange:{
        type: Boolean,
        required: false,
        default: false
      }
    },
    data(){
      return {
        arrayValue:!this.value?[]:this.value.split(",")
      }
    },
    watch:{
      value (val) {
        if(!val){
          this.arrayValue = []
        }else{
          this.arrayValue = this.value.split(",")
        }
      }
    },
    methods:{
      //下拉多谢组件
      filterOption(input, option){
        //console.log(input,'lxchun')
        //console.log(this.options,'lxchun1')
        //初始化拼音组件
        const PinyinMatch = require('pinyin-match');
        let p_m = PinyinMatch.match(option.componentOptions.children[0].text.toLowerCase(),input.toLowerCase())
        //console.log(p_m,'p_m')
        if(p_m){
          return true
        }else{
          return option.componentOptions.children[0].text.toLowerCase().indexOf(input.toLowerCase()) >= 0
        }
      },
      onChange (selectedValue) {
        if(this.triggerChange){
          this.$emit('change', selectedValue.join(","));
        }else{
          this.$emit('input', selectedValue.join(","));
        }
      },
    },

  }
</script>
