import { userResource } from "@/data/user"
import { createRouter, createWebHistory } from "vue-router"
import { session } from "./data/session"

const routes = [
	{
		path: "/",
		name: "Home",
		component: () => import("@/pages/Home.vue"),
	},
	{
		path: "/dashboard",
		name: "Dashboard",
		component: () => import("@/pages/Dashboard.vue"),
	},
	{
		path: "/service",
		name: "Service",
		component: () => import("@/pages/Service.vue"),
	},
	{
		path: "/invoice",
		name: "Invoice",
		component: () => import("@/pages/Invoice.vue"),
	},
	{
		path: "/order",
		name: "Order",
		component: () => import("@/pages/Order.vue"),
	},
	// {
	// 	name: "Login",
	// 	path: "/account/login",
	// 	component: () => import("@/pages/Login.vue"),
	// },
]

const router = createRouter({
	history: createWebHistory("/frontend"),
	routes,
})

router.beforeEach(async (to, from, next) => {
	let isLoggedIn = session.isLoggedIn
	try {
		await userResource.promise
	} catch (error) {
		isLoggedIn = false
	}

	if (to.name === "Login" && isLoggedIn) {
		next({ name: "Home" })
	} else if (to.name !== "Login" && !isLoggedIn) {
		next({ name: "Login" })
	} else {
		next()
	}
})

export default router
