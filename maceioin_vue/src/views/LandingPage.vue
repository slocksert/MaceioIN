<template>
  <div class="landing-page">
    <PageHeader />
    <main class="main-content">
      <HeroSection />
      <AboutSefazSection />
      <SefazActivitiesSection />
    </main>
    <PageFooter />
  </div>
</template>

<script>
import PageHeader from '../components/PageHeader.vue';
import PageFooter from '../components/PageFooter.vue';
import HeroSection from '../components/IntroSection.vue';
import AboutSefazSection from '../components/AboutSefaz.vue';
import SefazActivitiesSection from '../components/SefazActivities.vue';

export default {
  components: {
    PageHeader,
    PageFooter,
    HeroSection,
    AboutSefazSection,
    SefazActivitiesSection
  }
};
</script>

<style>
html, body, .landing-page {
  height: 100%;
  margin: 0;
}

.landing-page {
  display: flex;
  flex-direction: column;
}
</style>