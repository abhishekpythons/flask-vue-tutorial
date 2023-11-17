<template>
  <div class="about">
    <h1>
      This is a test app made to implement Asynchronous web application.
      <button type="submit" on-click="">submit</button>
      {{ path_link }}
    </h1>
  </div>
</template>

<script>
// import axios from "axios";
export default {
  data() {
    return {
      games: [],
      addGameForm: {
        path_link: "hello",
        genre: "",
        played: [],
      },
    };
  },

  methods: {
    pathTest() {
      const path = this.$route.query.page;
      this.path_link = path;
      console.log(path);
    },
  },
};
</script>
