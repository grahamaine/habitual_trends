import {Fragment,useCallback,useContext,useEffect} from "react"
import {Box as RadixThemesBox,Button as RadixThemesButton,Checkbox as RadixThemesCheckbox,Flex as RadixThemesFlex,Grid as RadixThemesGrid,Heading as RadixThemesHeading,Link as RadixThemesLink,Separator as RadixThemesSeparator,Text as RadixThemesText,TextField as RadixThemesTextField} from "@radix-ui/themes"
import {Activity as LucideActivity,BarChart3 as LucideBarChart3,Hexagon as LucideHexagon,LayoutDashboard as LucideLayoutDashboard,Plus as LucidePlus,Settings as LucideSettings} from "lucide-react"
import {Link as ReactRouterLink} from "react-router"
import {EventLoopContext,StateContexts} from "$/utils/context"
import {ReflexEvent} from "$/utils/state"
import {jsx} from "@emotion/react"




function Heading_a4037111931a035f4baff043f6431b54 () {
  const reflex___state____state__habitual_trends___habitual_trends____state = useContext(StateContexts.reflex___state____state__habitual_trends___habitual_trends____state)



  return (
    jsx(RadixThemesHeading,{css:({ ["color"] : "white", ["fontWeight"] : "bold" }),size:"8"},reflex___state____state__habitual_trends___habitual_trends____state.streak_rx_state_)
  )
}


function Heading_acac9ac14553dfb32514545119b7b41e () {
  const reflex___state____state__habitual_trends___habitual_trends____state = useContext(StateContexts.reflex___state____state__habitual_trends___habitual_trends____state)



  return (
    jsx(RadixThemesHeading,{css:({ ["color"] : "white", ["fontWeight"] : "bold" }),size:"8"},reflex___state____state__habitual_trends___habitual_trends____state.completion_rate_rx_state_)
  )
}


function Flex_075631fff85aa59952b9c913e3c18239 () {
  const reflex___state____state__habitual_trends___habitual_trends____state = useContext(StateContexts.reflex___state____state__habitual_trends___habitual_trends____state)



  return (
    jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"3"},Array.prototype.map.call(reflex___state____state__habitual_trends___habitual_trends____state.habits_rx_state_ ?? [],((habit_name_rx_state_,index_9b352df8a3c7917a89b120059976cc20)=>(jsx(RadixThemesBox,{css:({ ["padding"] : "1em", ["width"] : "100%", ["background"] : "rgba(255, 255, 255, 0.05)", ["backdropFilter"] : "blur(12px)", ["border"] : "1px solid rgba(255, 255, 255, 0.1)", ["borderRadius"] : "12px" }),key:index_9b352df8a3c7917a89b120059976cc20},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%", ["alignItems"] : "center" }),direction:"row",gap:"4"},jsx(RadixThemesText,{as:"label",size:"2"},jsx(RadixThemesFlex,{gap:"2"},jsx(RadixThemesCheckbox,{color:"cyan",size:"2"},),"")),jsx(RadixThemesText,{as:"p",css:({ ["color"] : "white" }),size:"3",weight:"medium"},habit_name_rx_state_),jsx(RadixThemesFlex,{css:({ ["flex"] : 1, ["justifySelf"] : "stretch", ["alignSelf"] : "stretch" })},),jsx(LucideActivity,{css:({ ["color"] : "var(--cyan-9)" }),size:18},)))))))
  )
}


function Button_ceb8e56eb830a84a777601bd07129a32 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_d4c30ac88b69cf2a89f7dd887f7894d4 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.habitual_trends___habitual_trends____state.add_habit", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["color"] : "cyan.400", ["borderColor"] : "cyan.400", ["marginTop"] : "2em", ["&:hover"] : ({ ["background"] : "rgba(0, 255, 255, 0.1)" }) }),onClick:on_click_d4c30ac88b69cf2a89f7dd887f7894d4,variant:"outline"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"row",gap:"3"},jsx(LucidePlus,{},),jsx(RadixThemesText,{as:"p"},"Add Habit")))
  )
}


export default function Component() {





  return (
    jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["bgImage"] : "url('/dashboard_bg.jpg')", ["bgSize"] : "cover", ["bgPosition"] : "center", ["bgRepeat"] : "no-repeat", ["height"] : "100vh", ["width"] : "100vw", ["overflow"] : "hidden" })},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["height"] : "100vh", ["alignItems"] : "start" }),direction:"row",gap:"0"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["background"] : "rgba(0, 9, 20, 0.85)", ["backdropFilter"] : "blur(15px)", ["borderRight"] : "1px solid rgba(255,255,255,0.1)", ["padding"] : "2em", ["height"] : "100vh", ["width"] : "300px", ["alignItems"] : "center" }),direction:"column",gap:"3"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "center", ["marginBottom"] : "2em" }),direction:"column",gap:"1"},jsx(LucideHexagon,{css:({ ["color"] : "var(--cyan-9)" }),size:40},),jsx(RadixThemesHeading,{css:({ ["color"] : "white", ["letterSpacing"] : "1px" }),size:"3"},"HABITUAL TRENDS"),jsx(RadixThemesText,{as:"p",css:({ ["color"] : "cyan.400", ["letterSpacing"] : "2px" }),size:"2"},"AI AGENT")),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"3"},jsx(RadixThemesTextField.Root,{css:({ ["background"] : "rgba(0,0,0,0.3)", ["borderColor"] : "gray.700", ["color"] : "white" }),placeholder:"Email"},),jsx(RadixThemesTextField.Root,{css:({ ["background"] : "rgba(0,0,0,0.3)", ["borderColor"] : "gray.700", ["color"] : "white" }),placeholder:"Password",type:"password"},),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"row",gap:"3"},jsx(RadixThemesFlex,{css:({ ["flex"] : 1, ["justifySelf"] : "stretch", ["alignSelf"] : "stretch" })},),jsx(RadixThemesLink,{css:({ ["color"] : "gray.400", ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) }),href:"#",size:"1"},"Forgot Password?")),jsx(RadixThemesButton,{css:({ ["background"] : "cyan.400", ["color"] : "black", ["width"] : "100%", ["&:hover"] : ({ ["background"] : "cyan.500" }) }),size:"3"},"Login"),jsx(RadixThemesButton,{css:({ ["color"] : "white", ["borderColor"] : "gray.600", ["width"] : "100%", ["&:hover"] : ({ ["background"] : "rgba(255,255,255,0.05)" }) }),size:"3",variant:"outline"},"Sign Up")),jsx(RadixThemesSeparator,{css:({ ["marginTop"] : "2em", ["marginBottom"] : "2em", ["borderColor"] : "gray.700" }),size:"4"},),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"2"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["padding"] : "0.8em", ["width"] : "100%", ["borderRadius"] : "8px", ["&:hover"] : ({ ["background"] : "rgba(255,255,255,0.1)" }), ["cursor"] : "pointer" }),direction:"row",gap:"3"},jsx(LucideLayoutDashboard,{css:({ ["color"] : "white" }),size:20},),jsx(RadixThemesText,{as:"p",css:({ ["color"] : "gray.300" }),size:"3",weight:"medium"},"Dashboard")),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["padding"] : "0.8em", ["width"] : "100%", ["borderRadius"] : "8px", ["&:hover"] : ({ ["background"] : "rgba(255,255,255,0.1)" }), ["cursor"] : "pointer" }),direction:"row",gap:"3"},jsx(LucideBarChart3,{css:({ ["color"] : "white" }),size:20},),jsx(RadixThemesText,{as:"p",css:({ ["color"] : "gray.300" }),size:"3",weight:"medium"},"Analytics")),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["padding"] : "0.8em", ["width"] : "100%", ["borderRadius"] : "8px", ["&:hover"] : ({ ["background"] : "rgba(255,255,255,0.1)" }), ["cursor"] : "pointer" }),direction:"row",gap:"3"},jsx(LucideSettings,{css:({ ["color"] : "white" }),size:20},),jsx(RadixThemesText,{as:"p",css:({ ["color"] : "gray.300" }),size:"3",weight:"medium"},"Settings")))),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["paddingInlineStart"] : "3em", ["paddingInlineEnd"] : "3em", ["paddingTop"] : "2em", ["paddingBottom"] : "2em", ["width"] : "100%", ["alignItems"] : "start" }),direction:"column",gap:"3"},jsx(RadixThemesHeading,{css:({ ["color"] : "white" }),size:"8",weight:"bold"},"Welcome back, Graham"),jsx(RadixThemesGrid,{columns:"3",css:({ ["width"] : "100%", ["marginTop"] : "2em", ["marginBottom"] : "2em" }),gap:"4"},jsx(RadixThemesBox,{css:({ ["padding"] : "1.5em", ["width"] : "100%", ["background"] : "rgba(255, 255, 255, 0.05)", ["backdropFilter"] : "blur(12px)", ["border"] : "1px solid rgba(255, 255, 255, 0.1)", ["borderRadius"] : "12px" })},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "start" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "gray.300" }),size:"2",weight:"medium"},"Current Streak"),jsx(Heading_a4037111931a035f4baff043f6431b54,{},))),jsx(RadixThemesBox,{css:({ ["padding"] : "1.5em", ["width"] : "100%", ["background"] : "rgba(255, 255, 255, 0.05)", ["backdropFilter"] : "blur(12px)", ["border"] : "1px solid rgba(255, 255, 255, 0.1)", ["borderRadius"] : "12px" })},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "start" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "gray.300" }),size:"2",weight:"medium"},"Completion"),jsx(Heading_acac9ac14553dfb32514545119b7b41e,{},))),jsx(RadixThemesBox,{css:({ ["padding"] : "1.5em", ["width"] : "100%", ["background"] : "rgba(255, 255, 255, 0.05)", ["backdropFilter"] : "blur(12px)", ["border"] : "1px solid rgba(255, 255, 255, 0.1)", ["borderRadius"] : "12px" })},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "start" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "gray.300" }),size:"2",weight:"medium"},"Total Habits"),jsx(RadixThemesHeading,{css:({ ["color"] : "white", ["fontWeight"] : "bold" }),size:"8"},"3")))),jsx(RadixThemesHeading,{css:({ ["color"] : "white", ["marginTop"] : "1em", ["marginBottom"] : "0.5em" }),size:"6"},"Your Habits"),jsx(Flex_075631fff85aa59952b9c913e3c18239,{},),jsx(Button_ceb8e56eb830a84a777601bd07129a32,{},)))),jsx("title",{},"HabitualTrends | Index"),jsx("meta",{content:"favicon.ico",property:"og:image"},))
  )
}