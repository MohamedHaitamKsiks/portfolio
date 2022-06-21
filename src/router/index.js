import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ProjectsView from '../views/ProjectsView.vue'
import PageNotFoundView from '../views/PageNotFoundView.vue'
import FreelanceView from '../views/FreelanceView.vue'
import AboutView from '../views/AboutView.vue'

const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes: [
		{
			path: '/',
			name: 'home',
			component: HomeView
		}, 
		{
			path: '/projects',
			name: 'projects',
			component: ProjectsView
		}, 
		{
			path: '/freelance',
			name: 'freelance',
			component: FreelanceView
		}, 
		{
			path: '/about',
			name: 'about',
			component: AboutView
		},
		{
			path: '/:pathMatch(.*)*',
			name: 'PageNotFound',
			component: PageNotFoundView
		}
	]
})

export default router
