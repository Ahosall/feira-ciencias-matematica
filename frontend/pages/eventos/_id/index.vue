<template>
  <v-card class="mx-auto">
    <v-card-title>{{ evento.descricao }}</v-card-title>

    <v-card-text>
      <h3>Projeto : {{ projeto.descricao }}</h3>
      <div v-for="pp in participanteProjeto" :key="pp.id">
          <h3>Alunos : {{ pp.participante }}</h3>
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  head() {
    return {
      title: "View Alunos"
    };
  },
  async asyncData({ $axios, params }) {
    try {
      let evento = await $axios.$get(`/eventos/${params.id}`);

      let projeto = await $axios.$get(`/projetos/${evento.projeto}`);

      let participanteProjeto = await $axios.$get(`/participantes-projetos/?evento=${params.id}`);

      //let participantes = await $axios.$get(`/participantes/?grupo=${participanteProjeto.participante}`);
      
      return { evento, projeto, participanteProjeto };
    } catch (e) {
      return { evento: [], projeto: [], participanteProjeto: [] };
    }
  },
  data() {
    return {
      evento: {
        descricao: "",
        projeto: ""
      },
      projeto: {
        id: "",
        descricao: ""
      },
      participanteProjeto: {
        id: "",
        participante: ""
      }
    };
  }
};
</script>