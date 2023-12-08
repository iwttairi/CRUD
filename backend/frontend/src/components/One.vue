<template>
  <div class="hello">
    <div class="title-color">hh [[ message ]] hh</div>
    <table width="600">
      <tr>
        <th>username</th>
        <th>email address</th>
      </tr>
      <tr v-for="user in users" v-bind:key="user.id">
        <td>[[ user.username ]]</td>
        <td>[[ user.email ]]</td>
        <td><button v-on:click="deleteUser(user.id)">Delete</button></td>
      </tr>
    </table>
    <button v-on:click="createUser">Add new user</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "OneView",
  props: {
    msg: String,
  },
  data() {
    return {
      message: "",
      users: [],
    };
  },
  mounted() {
    this.getUser();
  },
  methods: {
    getUser() {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/user/",
        auth: {
          username: "superuser",
          password: "airiairiairi",
        },
      }).then((response) => {
        console.log("hello");
        console.log(response);
        this.message = "hello!!";
        this.users = response.data;
        console.log(this.users);
      });
    },
    createUser() {
      this.$router.push("/two")
    },
    deleteUser(id) {
      axios({
        method: "delete",
        url: "http://127.0.0.1:8000/user/" + id + "/",
        auth: {
          username: "superuser",
          password: "airiairiairi",
        },
      }).then((response) => {
        console.log(response);
        this.$router.go({path: this.$router.currentRoute.path, force: true});
      });
    },
  },
};
</script>

<style scoped>
.title-color {
  color: green;
}
</style>
