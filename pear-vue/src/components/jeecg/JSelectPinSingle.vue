<template>
  <a-select
    showSearch
    placeholder="Select a person"
    optionFilterProp="children"
    style="width: 200px"
    @search="handleSearch"
    @change="handleChange"
    :notFoundContent="null"
  >
  <a-select-option
      v-for="(item,index) in options"
      :key="index"
      :value="item.value">
      {{ item.text || item.label }}
    </a-select-option>
  </a-select>
</template>
<script>
  import {postAction} from '@/api/manage'

  export default {
    name: 'JSelectPinSingle',
    methods: {
       data() {
        return {
          options: [],
          value: undefined,
        };
      },
      handleChange(value) {
        console.log(`selected ${value}`);
      },
      handleBlur() {
        console.log('blur');
      },
      handleFocus() {
        console.log('focus');
      },
      filterOption(input, option) {
        
      },
    },
  };
</script>
