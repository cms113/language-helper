<template>
  <v-container>
    <v-row v-if="pending" justify="center">
      <v-progress-circular indeterminate size="50" color="blue" />
    </v-row>
    <v-row v-else align="center" justify="center">
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
            <v-form ref="form" lazy-validation v-model="valid">
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
import { reactive, computed, ref } from "vue";
const { $unsplash } = useNuxtApp();
const form = ref(null);
const route = useRoute();
const id = route.params.id;

const { pending, data: cards } = useLazyFetch(
  `http://localhost:8000/api/deck/${id}`
);

interface QuestionAnswer {
  question: string;
  response: string;
  answer: string;
  imageURL: string;
}

const index = ref(0);
const valid = ref(false);

const currentCard = computed(() => {
  if (pending.value === true) {
    return null;
  }
  return cards.value[index.value];
});

watch(currentCard, async (newVal) => {
  console.log(newVal);
  if (currentCard.value?.imageURL === "") {
    currentCard.value.imageURL = await getImage();
  }
});

function checkAnswer() {
  form.value.validate();
  if (valid.value) {
    index.value++;
  }
}

async function getImage() {
  try {
    var keyword = currentCard.value.question;
    var photos = await $unsplash.search.getPhotos({ query: keyword });
    return photos.response.results[0].urls.full;
  } catch (err) {
    console.log(err);
  }
}
</script>

<style scoped></style>
