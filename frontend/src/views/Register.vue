<template>
  <v-app>
    <v-card width="800" color="#EEEEEE" class="mx-auto my-auto elevation-12">
      <v-card-title>
        <h1 class="display-1 mx-auto">Registration</h1>
      </v-card-title>
      <v-container
        id="scroll-target"
        style="max-height: 700px"
        class="overflow-y-auto"
      >
        <v-row
          v-scroll:#scroll-target="onScroll"
          align="top"
          justify="center"
        >
          <v-card-text>
            <v-text-field 
              label="Username"
              v-model="username"
              prepend-icon="mdi-account-circle"
            />
            <v-text-field 
              label="E-mail"
              v-model="email"
              prepend-icon="mdi-email"
              :rules="emailRules"
            />
            <v-text-field 
              label="Password"
              :type="showPassword ? 'text' : 'password'"
              v-model.lazy="password"
              prepend-icon="mdi-lock"
              :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
              @click:append="showPassword = !showPassword"
              :rules="passwordRules"
              required
            />
            <v-text-field 
              label="Confirm Password"
              :type="showPassword2 ? 'text' : 'password'"
              v-model.lazy="password2"
              prepend-icon="mdi-lock"
              :append-icon="showPassword2 ? 'mdi-eye' : 'mdi-eye-off'"
              @click:append="showPassword2 = !showPassword2"
              :rules="passwordConfirmRules"
              required
            />

            <v-radio-group v-model="radioGroup">
              <v-radio
                label="男性"
                value="1"
              ></v-radio>
              <v-radio
                label="女性"
                value="2"
              ></v-radio>
            </v-radio-group>

            <v-row>
              <v-col
                cols="12"
                md="4"
              >
                <v-text-field
                  v-model="year"
                  :rules="nameRules"
                  label="Year"
                  required
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                md="4"
              >
                <v-text-field
                  v-model="month"
                  :rules="monthRules"
                  label="Month"
                  required
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                md="4"
              >
                <v-text-field
                  v-model="day"
                  :rules="dayRules"
                  label="Day"
                  required
                ></v-text-field>
              </v-col>
            </v-row>

            <v-select
              :items="places"
              label="Solo field"
              solo
            ></v-select>
<!-- ここは取り換え -->
            <v-select
              :items="places"
              label="Course"
              multiple
              solo
              chips
            ></v-select>

            <v-textarea
              solo
              name="textarea"
              label="※任意"
            ></v-textarea>

            <v-alert 
              v-if="registerError"
              color="red" 
              text="true"
              class="elevation-2"
              icon="mdi-alert"
            >you cannot sign up!</v-alert>
          </v-card-text>
          <v-card-actions>
            <v-row align="center" justify="center" class="mb-5" >
              <v-btn  to="login" color="success" class="mr-5">Login</v-btn>
              <v-btn  @click.prevent="registration">Sign Up</v-btn>
            </v-row>
          </v-card-actions>

        </v-row>
      </v-container>
    </v-card>
  </v-app>
</template>

<script>
export default {
  name:"Register",
    data() {
    return{
      places: ['東京','福岡','名古屋'],
      snackbar: false,
      snackbar_msg: ""
    }
  }
}
</script>