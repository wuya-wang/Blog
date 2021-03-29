<template>
  <div id="wakatime">
    <div>
    <el-row>
      <el-col :xs="24" :sm="24" :md="12" :lg="12" :xl="12">
        <figure><embed src="https://wakatime.com/share/@8e33fc72-2aa9-478d-a8c0-e4e97b54f6f9/8a935e96-44a7-44bb-9aab-d1576199f8cc.svg"></figure>
      </el-col>
      <el-col :xs="24" :sm="24" :md="12" :lg="12" :xl="12">
        <figure><embed src="https://wakatime.com/share/@8e33fc72-2aa9-478d-a8c0-e4e97b54f6f9/5c12556d-f917-4be9-989a-e31cf128c2aa.svg"></figure>
      </el-col>
    </el-row>
    <el-row >
      <el-col :xs="24" :sm="24" :md="12" :lg="12" :xl="12">
        <figure class="wakatime_editors"><embed src="https://wakatime.com/share/@8e33fc72-2aa9-478d-a8c0-e4e97b54f6f9/f6769196-724e-47d0-8764-726663143e76.svg"></figure>
      </el-col>
      <el-col :xs="24" :sm="24" :md="12" :lg="12" :xl="12">
        <figure class="wakatime_categories"><embed src="https://wakatime.com/share/@8e33fc72-2aa9-478d-a8c0-e4e97b54f6f9/773ba8e9-e101-45d1-b6d5-f24ecd582609.svg"></figure>
      </el-col>
    </el-row>
    </div>
  </div>
</template>

<script>
export default {
name: "WakaTime"
}
</script>

<style scoped>
figure{
  padding: 1rem;
  margin: 0;
}
</style>