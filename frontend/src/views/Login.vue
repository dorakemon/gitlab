<template>
  <!-- <div>
    <h2>ログイン</h2>
    <form @submit.prevent="login">
      <div class="username">
        <label for="username">ユーザーネーム</label>
        <input type="text" v-model="username" class="form-control">
      </div>
      <div class="password pb-3">
        <label for="password">パスワード</label>
        <input type="password" v-model="password" class="form-control">
      </div>
      <button type="submit" class="btn btn-success">ログイン</button>
  </form>
  </div> -->
  <v-app style="background:linear-gradient(-135deg, #667eea, #764ba2)">
    <v-card width="400" color="#EEEEEE" class="mx-auto my-auto elevation-12">
      <v-card-title>
        <h1 class="display-1 mx-auto">Login</h1>
      </v-card-title>
      <v-card-text>
        <v-text-field 
          label="Username"
          v-model.lazy="username"
          prepend-icon="mdi-account-circle"
        />
        <v-text-field 
          label="Password"
          :type="showPassword ? 'text' : 'password'"
          v-model.lazy="password"
          prepend-icon="mdi-lock"
          :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
          @click:append="showPassword = !showPassword"
        />
        <v-alert 
          v-if="$store.getters.error"
          color="red" 
          text="true"
          class="elevation-2"
          icon="mdi-alert"
        >{{ errorMessage }}</v-alert>
      </v-card-text>
      
      <v-card-actions class=" mb-5">
        <v-row align="center" justify="center" >
          <v-btn  @click.prevent="login" color="success" class="mr-5">Login</v-btn>
          <v-btn  to="register" color="info">SignUp</v-btn>
        </v-row>
      </v-card-actions>
    </v-card>
  </v-app>
</template>

<script>
export default {
  name:"Login"
}
</script>