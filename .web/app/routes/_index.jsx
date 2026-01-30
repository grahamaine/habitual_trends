import {Fragment,useCallback,useContext,useEffect} from "react"
import {Button as RadixThemesButton,Flex as RadixThemesFlex,Grid as RadixThemesGrid,Heading as RadixThemesHeading,Link as RadixThemesLink,Text as RadixThemesText,TextField as RadixThemesTextField} from "@radix-ui/themes"
import {Activity as LucideActivity,BarChart2 as LucideBarChart2,LayoutDashboard as LucideLayoutDashboard,Settings as LucideSettings} from "lucide-react"
import {EventLoopContext,StateContexts} from "$/utils/context"
import {ReflexEvent} from "$/utils/state"
import {Link as ReactRouterLink} from "react-router"
import {jsx} from "@emotion/react"




function Textfield__root_067c48a0d6b63c3ac3d503cdeb5bad63 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_37e90813944988a3cd76bf9e4f173fe1 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.habitual_trends___habitual_trends____state.set_email", ({ ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesTextField.Root,{css:({ ["background"] : "transparent", ["border"] : "1px solid #334", ["color"] : "white" }),onChange:on_change_37e90813944988a3cd76bf9e4f173fe1,placeholder:"Email"},)
  )
}


function Textfield__root_22afa51589bf17f6bbbe68131b0d1845 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_1513a8a1644c5e67152de1b16f289cad = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.habitual_trends___habitual_trends____state.set_password", ({ ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesTextField.Root,{css:({ ["background"] : "transparent", ["border"] : "1px solid #334", ["color"] : "white" }),onChange:on_change_1513a8a1644c5e67152de1b16f289cad,placeholder:"Password",type:"password"},)
  )
}


function Button_d17563762dacea9f6be1881bcb9f3b06 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_7f8a5acf2146c9b29ecbd86e8276c8c2 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.habitual_trends___habitual_trends____state.handle_login", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "linear-gradient(90deg, #00f0ff, #0077ff)", ["color"] : "black", ["width"] : "100%", ["&:hover"] : ({ ["opacity"] : 0.8 }) }),onClick:on_click_7f8a5acf2146c9b29ecbd86e8276c8c2},"Login")
  )
}


function Button_7c2cccaee7b8294351fc0762e69b3f33 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_2a8126d9c1d7bc512177e6751f1707a3 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.habitual_trends___habitual_trends____state.increase_streak", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["color"] : "cyan", ["borderColor"] : "cyan", ["width"] : "100%", ["fontSize"] : "0.8em" }),onClick:on_click_2a8126d9c1d7bc512177e6751f1707a3,variant:"outline"},"Test: Add Streak +1")
  )
}


function Text_f8f61281b98585ccd9cb0dc0057eb0e8 () {
  const reflex___state____state__habitual_trends___habitual_trends____state = useContext(StateContexts.reflex___state____state__habitual_trends___habitual_trends____state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : "cyan", ["fontSize"] : "2em", ["fontWeight"] : "bold" })},reflex___state____state__habitual_trends___habitual_trends____state.streak_rx_state_)
  )
}


function Text_1fa523d1181fd926b7aca5066be40e89 () {
  const reflex___state____state__habitual_trends___habitual_trends____state = useContext(StateContexts.reflex___state____state__habitual_trends___habitual_trends____state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : "cyan", ["fontSize"] : "2em", ["fontWeight"] : "bold" })},reflex___state____state__habitual_trends___habitual_trends____state.completion_rx_state_)
  )
}


function Text_ac830079f26c000f42d9c710d2aaa3bc () {
  const reflex___state____state__habitual_trends___habitual_trends____state = useContext(StateContexts.reflex___state____state__habitual_trends___habitual_trends____state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : "cyan", ["fontSize"] : "2em", ["fontWeight"] : "bold" })},reflex___state____state__habitual_trends___habitual_trends____state.total_habits_rx_state_)
  )
}


export default function Component() {





  return (
    jsx(Fragment,{},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"row",gap:"0"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["background"] : "#0B1120", ["height"] : "100vh", ["width"] : "350px", ["padding"] : "2em", ["alignItems"] : "center", ["borderRight"] : "1px solid #1f2937", ["@media screen and (min-width: 0)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 30em)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 48em)"] : ({ ["display"] : "flex" }), ["@media screen and (min-width: 62em)"] : ({ ["display"] : "flex" }) }),direction:"column",gap:"3"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "center", ["paddingBottom"] : "3em" }),direction:"column",gap:"1"},jsx(LucideActivity,{css:({ ["color"] : "cyan" }),size:40},),jsx(RadixThemesHeading,{css:({ ["color"] : "cyan", ["letterSpacing"] : "2px" }),size:"4"},"HABITUAL TRENDS"),jsx(RadixThemesText,{as:"p",css:({ ["color"] : "white", ["letterSpacing"] : "4px" }),size:"1"},"AI AGENT")),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%", ["paddingBottom"] : "3em" }),direction:"column",gap:"4"},jsx(Textfield__root_067c48a0d6b63c3ac3d503cdeb5bad63,{},),jsx(Textfield__root_22afa51589bf17f6bbbe68131b0d1845,{},),jsx(RadixThemesLink,{css:({ ["color"] : "gray", ["fontSize"] : "0.8em", ["alignSelf"] : "end", ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) }),href:"#"},"Forgot Password?"),jsx(Button_d17563762dacea9f6be1881bcb9f3b06,{},),jsx(Button_7c2cccaee7b8294351fc0762e69b3f33,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "start", ["width"] : "100%" }),direction:"column",gap:"6"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["cursor"] : "pointer" }),direction:"row",gap:"3"},jsx(LucideLayoutDashboard,{css:({ ["color"] : "cyan" })},),jsx(RadixThemesText,{as:"p",css:({ ["color"] : "white" })},"Dashboard")),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["cursor"] : "pointer" }),direction:"row",gap:"3"},jsx(LucideBarChart2,{css:({ ["color"] : "cyan" })},),jsx(RadixThemesText,{as:"p",css:({ ["color"] : "white" })},"Analytics")),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["cursor"] : "pointer" }),direction:"row",gap:"3"},jsx(LucideSettings,{css:({ ["color"] : "cyan" })},),jsx(RadixThemesText,{as:"p",css:({ ["color"] : "white" })},"Settings")))),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["bgImage"] : "url('/dashboard_bg.jpg')", ["bgSize"] : "cover", ["bgPosition"] : "center", ["width"] : "100%", ["height"] : "100vh", ["padding"] : "3em" }),direction:"column",gap:"5"},jsx(RadixThemesHeading,{css:({ ["color"] : "white", ["marginBottom"] : "1em" }),size:"8"},"Welcome back, Graham"),jsx(RadixThemesGrid,{columns:"3",css:({ ["width"] : "100%" }),gap:"5"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["background"] : "rgba(18, 25, 45, 0.8)", ["backdropFilter"] : "blur(10px)", ["padding"] : "1.5em", ["borderRadius"] : "15px", ["border"] : "1px solid rgba(255, 255, 255, 0.1)", ["width"] : "100%", ["alignItems"] : "start", ["boxShadow"] : "0 4px 30px rgba(0, 0, 0, 0.5)" }),direction:"column",gap:"3"},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#a0aec0", ["fontSize"] : "0.9em", ["fontWeight"] : "bold" })},"Current Streak"),jsx(Text_f8f61281b98585ccd9cb0dc0057eb0e8,{},),jsx(RadixThemesText,{as:"p",css:({ ["color"] : "white", ["fontSize"] : "0.8em" })},"Days in a row")),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["background"] : "rgba(18, 25, 45, 0.8)", ["backdropFilter"] : "blur(10px)", ["padding"] : "1.5em", ["borderRadius"] : "15px", ["border"] : "1px solid rgba(255, 255, 255, 0.1)", ["width"] : "100%", ["alignItems"] : "start", ["boxShadow"] : "0 4px 30px rgba(0, 0, 0, 0.5)" }),direction:"column",gap:"3"},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#a0aec0", ["fontSize"] : "0.9em", ["fontWeight"] : "bold" })},"Completion"),jsx(Text_1fa523d1181fd926b7aca5066be40e89,{},),jsx(RadixThemesText,{as:"p",css:({ ["color"] : "white", ["fontSize"] : "0.8em" })},"All tasks done")),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["background"] : "rgba(18, 25, 45, 0.8)", ["backdropFilter"] : "blur(10px)", ["padding"] : "1.5em", ["borderRadius"] : "15px", ["border"] : "1px solid rgba(255, 255, 255, 0.1)", ["width"] : "100%", ["alignItems"] : "start", ["boxShadow"] : "0 4px 30px rgba(0, 0, 0, 0.5)" }),direction:"column",gap:"3"},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#a0aec0", ["fontSize"] : "0.9em", ["fontWeight"] : "bold" })},"Total Habits"),jsx(Text_ac830079f26c000f42d9c710d2aaa3bc,{},),jsx(RadixThemesText,{as:"p",css:({ ["color"] : "white", ["fontSize"] : "0.8em" })},"Active habits"))))),jsx("title",{},"HabitualTrends | Index"),jsx("meta",{content:"favicon.ico",property:"og:image"},))
  )
}