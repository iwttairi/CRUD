<template>
  <div class="hello">
    <div class="title-color">This is a create page.</div>
      <div class="form-container">
        <form v-on:submit.prevent="addUser">
          <h2>Add User</h2>
          <div class="form-group">
            <label class="label">username</label>
            <input class="input" type="text" v-model="username" /><br>
          </div>
          <div class="form-group">
            <label class="label">email</label>
            <input class="input" type="text" v-model="email" /><br>
          </div>
          <div class="form-group">
            <label class="label">password</label>
            <input class="input" type="text" v-model="password" /><br>
          </div>
          <button class="button" type="submit">Submit</button>
        </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "TwoView",
  props: {
    msg: String,
  },
  data() {
    return {
      username: "",
      email: "",
      password: "",
    };
  },
  mounted() {
  },
  methods: {
    addUser() {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/user/",
        data: {
          username: this.username,
          email: this.email,
          password: this.password,
        },
        auth: {
          username: "superuser",
          password: "airiairiairi",
        },
      }).then(() => {
        this.$router.push("/one")
      })
    }
  }
};
</script>

<style scoped>
.title-color {
  color: blue;
}

.form-container {
  max-width: 400px;
  margin: 0 auto;
}
.form-group {
  margin-bottom: 15px;
}

.label {
  display: block;
  margin-bottom: 5px;
}

.input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.button {
  display: block;
  text-align: center;
	text-decoration: none;
	margin: auto;
	padding: 1rem 4rem;
	font-weight: bold;
	border: 2px solid #27acd9;
	color: #27acd9;
	border-radius: 100vh;
	transition: 0.5s;
}
</style>