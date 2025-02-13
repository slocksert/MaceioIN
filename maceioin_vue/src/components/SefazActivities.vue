<template>
    <section class="sefaz-activities">
      <h3>Principais Atividades</h3>
      <div class="activity-cards">
        <div class="activity-card" v-for="activity in activities" :key="activity.title">
          <h4>{{ activity.title }}</h4>
          <p>{{ activity.description }}</p>
        </div>
      </div>
    </section>
  </template>
  
<script>
  export default {
    name: 'SefazActivitiesSection',
    data() {
      return {
        activities: [
          { 
            title: 'Gestão da Arrecadação de Tributos', 
            description: 'Responsável pela administração e fiscalização dos tributos estaduais, garantindo a arrecadação eficiente e o cumprimento das obrigações fiscais.' 
        },
          { 
            title: 'Administração Financeira', 
            description: 'Gerencia as finanças do Estado, incluindo o planejamento orçamentário, controle de despesas e receitas, assegurando a saúde financeira pública.' 
        },
          { 
            title: 'Transparência Fiscal', 
            description: 'Promove a transparência na gestão fiscal, disponibilizando informações claras e acessíveis sobre a execução orçamentária e financeira do Estado.' 
        },
          { 
            title: 'Educação Tributária', 
            description: 'Desenvolve programas e ações educativas para conscientizar a população sobre a importância do cumprimento das obrigações tributárias.' 
        },
        ]
      };
    }
  };
</script>
  
<style scoped>
.sefaz-activities {
  padding: 20px;
  background: #f8f9fa;
}

.sefaz-activities h3 {
  text-align: center;
  color: #007BFF;
  margin-bottom: 30px;
}

.activity-cards {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  gap: 1rem;
}

.activity-card {
  background: #f1f1f1;
  border-radius: 8px;
  padding: 20px;
  width: 22%;
  margin: 0.5rem 0;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.activity-card:hover {
  transform: scale(1.05);
}

.activity-card h4 {
  color: #007BFF;
  margin-bottom: 10px;
}

.activity-card p {
  font-size: 0.9rem;
  line-height: 1.4;
}

@media (max-width: 768px) {
  .activity-cards{
    flex-direction: column;
    align-items: center;
  }

  .activity-card {
    width: 75%;
  }
}
</style>