<template>
  <v-container>
    <v-row align="center" justify="center">
      <v-col cols="auto">
        <v-card width="400px" rounded="lg" color="#1F7087" theme="dark">
          <v-card-title class="text-center text-h4 my-2">
            {{ currentCard.question }}
          </v-card-title>
          <v-img
            v-if="currentCard.imageURL"
            width="100%"
            aspect-ratio="1"
            :src="currentCard.imageURL"
          />
          <v-card-text>
            <v-form ref="form" lazy-validation v-model="options.valid">
              <v-text-field
                theme="default"
                placeholder="Answer here!"
                v-model="currentCard.response"
                :rules="[
                  (v) => v.toLowerCase() === currentCard.answer || 'Not quite!',
                ]"
                @input="form.resetValidation()"
              />
            </v-form>
          </v-card-text>

          <v-card-actions>
            <v-row justify="center">
              <v-btn
                variant="outlined"
                @click="checkAnswer"
                width="150px"
                color="white"
              >
                Submit
              </v-btn>
            </v-row>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { reactive, computed } from "vue";
const { $unsplash } = useNuxtApp();
const form = ref(null);

interface QuestionAnswer {
  question: string;
  response: string;
  answer: string;
  imageURL: string;
}

interface State {
  index: number;
  valid: boolean;
  cards: QuestionAnswer[];
}

var options = reactive<State>({
  index: 0,
  valid: false,
  cards: [
    { question: "The tree", answer: "L'albero", response: "", imageURL: "" },
    { question: "The cat", answer: "Il gatto", response: "", imageURL: "" },
    { question: "The dog", answer: "Il cane", response: "", imageURL: "" },
  ],
});

const currentCard = computed(() => options.cards[options.index]);

function checkAnswer() {
  form.value.validate();
  if (options.valid) {
    options.index++;
    getImage();
  }
}

async function getImage() {
  try {
    var keyword = currentCard.value.question;
    var photos = await $unsplash.search.getPhotos({ query: keyword });
    var firstPhoto = photos.response.results[0].urls.full;
    currentCard.value.imageURL = firstPhoto;
  } catch (err) {
    console.log(err);
  }
}

onMounted(getImage);
</script>

<style scoped></style>
