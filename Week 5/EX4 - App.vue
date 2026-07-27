<template>
  <div class="container">
    <h1>Vue 3 Reactive List & Filter</h1>

    <input
      v-model="search"
      type="text"
      placeholder="Search fruits..."
    />

    <ul>
      <li v-for="fruit in filteredFruits" :key="fruit">
        {{ fruit }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";

const search = ref("");

const fruits = ref([
  "Apple",
  "Banana",
  "Orange",
  "Mango",
  "Pineapple",
  "Grapes",
  "Watermelon"
]);

const filteredFruits = computed(() => {
  return fruits.value.filter(fruit =>
    fruit.toLowerCase().includes(search.value.toLowerCase())
  );
});
</script>

<style>
body{
  font-family: Arial, sans-serif;
  background:#f4f4f4;
}

.container{
  width:400px;
  margin:50px auto;
  background:white;
  padding:20px;
  border-radius:10px;
  box-shadow:0 0 10px rgba(0,0,0,0.2);
}

h1{
  color:#42b883;
  text-align:center;
}

input{
  width:100%;
  padding:10px;
  margin:15px 0;
  font-size:16px;
}

ul{
  list-style:none;
  padding:0;
}

li{
  background:#42b883;
  color:white;
  margin:8px 0;
  padding:10px;
  border-radius:5px;
}
</style>
