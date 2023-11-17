<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>
      For more visit Cart for worshop here
      <a href="http://127.0.0.1:8080/cart" target="_blank" rel="noopener"
        >/cart</a
      >.
    </p>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
